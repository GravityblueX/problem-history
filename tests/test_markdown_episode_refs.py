from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_markdown_episode_refs import (
    ReferenceError,
    validate_studies,
)  # noqa: E402


def episode(episode_id: str | None, predecessor: str | None = None) -> str:
    fields = []
    if episode_id is not None:
        fields.append(f"episode_id: {episode_id}")
    fields.extend(["problem_id: fixture", "period: 1950", "status: active"])
    if predecessor is not None:
        fields.append(f"predecessor: {predecessor}")
    return "# Fixture\n\n```yaml\n" + "\n".join(fields) + "\n```\n"


def readme(relations: list[tuple[str, str]]) -> str:
    declaration = "relations:" if relations else "relations: []"
    lines = ["# Fixture study", "", "```yaml", declaration]
    for source, target in relations:
        lines.extend(
            [
                f"  - from: {source}",
                f"    to: {target}",
                "    type: transformed_successor",
            ]
        )
    return "\n".join(lines + ["```", ""])


class MarkdownEpisodeReferenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.studies = Path(self.temporary.name) / "studies"
        self.study = self.studies / "fixture-study"
        (self.study / "episodes").mkdir(parents=True)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> None:
        (self.study / relative).write_text(content, encoding="utf-8")

    def valid_graph(
        self, names: tuple[str, str] = ("01_first.md", "02_second.md")
    ) -> None:
        self.write(f"episodes/{names[0]}", episode("first"))
        self.write(f"episodes/{names[1]}", episode("second", "first"))
        self.write("README.md", readme([("first", "second")]))

    def test_checked_in_study_is_valid(self) -> None:
        counts = validate_studies(REPO_ROOT / "studies")
        self.assertEqual(counts, {"episodes": 3, "relations": 2})

    def test_file_names_do_not_define_episode_identity(self) -> None:
        self.valid_graph(("renamed-later.md", "unrelated-file-name.md"))
        self.assertEqual(validate_studies(self.studies)["relations"], 1)

    def test_missing_episode_id_is_rejected(self) -> None:
        self.write("episodes/missing.md", episode(None))
        self.write("README.md", readme([]))
        with self.assertRaisesRegex(ReferenceError, "missing episode_id"):
            validate_studies(self.studies)

    def test_duplicate_episode_id_is_rejected(self) -> None:
        self.write("episodes/one.md", episode("same"))
        self.write("episodes/two.md", episode("same"))
        self.write("README.md", readme([]))
        with self.assertRaisesRegex(ReferenceError, "duplicate episode_id"):
            validate_studies(self.studies)

    def test_duplicate_metadata_key_is_rejected(self) -> None:
        duplicate = episode("first").replace(
            "episode_id: first", "episode_id: first\nepisode_id: second"
        )
        self.write("episodes/one.md", duplicate)
        self.write("README.md", readme([]))
        with self.assertRaisesRegex(ReferenceError, "duplicate metadata key"):
            validate_studies(self.studies)

    def test_metadata_keys_require_plain_separated_yaml(self) -> None:
        invalid_lines = {
            "compact": "episode_id:one",
            "non-breaking separation": "episode_id:\u00a0one",
            "quoted duplicate": 'episode_id: one\n"episode_id": two',
            "single-quoted duplicate": "episode_id: one\n'episode_id': two",
        }
        self.write("README.md", readme([]))
        for name, metadata in invalid_lines.items():
            with self.subTest(name=name):
                document = f"# Fixture\n\n```yaml\n{metadata}\n```\n"
                self.write("episodes/one.md", document)
                with self.assertRaises(ReferenceError):
                    validate_studies(self.studies)

    def test_unicode_whitespace_is_not_trimmed_from_slugs(self) -> None:
        self.write("README.md", readme([]))
        for name, value in {
            "leading NBSP": "\u00a0one",
            "trailing NBSP": "one\u00a0",
            "leading em space": "\u2003one",
            "trailing em space": "one\u2003",
        }.items():
            with self.subTest(name=name):
                self.write("episodes/one.md", episode(value))
                with self.assertRaisesRegex(
                    ReferenceError, "lowercase hyphenated slug"
                ):
                    validate_studies(self.studies)

    def test_identity_scalars_cannot_continue_on_indented_lines(self) -> None:
        self.write("README.md", readme([]))
        continued_id = episode("one").replace(
            "episode_id: one", "episode_id: one\n  suffix"
        )
        self.write("episodes/one.md", continued_id)
        with self.assertRaisesRegex(ReferenceError, "episode_id must be a single-line"):
            validate_studies(self.studies)

        self.write("episodes/one.md", episode("one"))
        continued_predecessor = episode("two", "one").replace(
            "predecessor: one", "predecessor: one\n  suffix"
        )
        self.write("episodes/two.md", continued_predecessor)
        self.write("README.md", readme([("one", "two")]))
        with self.assertRaisesRegex(
            ReferenceError, "predecessor must be a single-line"
        ):
            validate_studies(self.studies)

    def test_unresolved_predecessor_is_rejected(self) -> None:
        self.write("episodes/one.md", episode("one", "missing"))
        self.write("README.md", readme([]))
        with self.assertRaisesRegex(ReferenceError, "predecessor references unknown"):
            validate_studies(self.studies)

    def test_predecessor_must_have_a_readme_relation(self) -> None:
        self.write("episodes/one.md", episode("one"))
        self.write("episodes/two.md", episode("two", "one"))
        self.write("README.md", readme([]))
        with self.assertRaisesRegex(ReferenceError, "not backed by a README relation"):
            validate_studies(self.studies)

    def test_unresolved_readme_endpoints_are_rejected(self) -> None:
        self.write("episodes/one.md", episode("one"))
        self.write("README.md", readme([("missing", "one"), ("one", "absent")]))
        with self.assertRaises(ReferenceError) as context:
            validate_studies(self.studies)
        message = str(context.exception)
        self.assertIn("relation from references unknown episode 'missing'", message)
        self.assertIn("relation to references unknown episode 'absent'", message)

    def test_duplicate_and_self_relations_are_rejected(self) -> None:
        self.write("episodes/one.md", episode("one"))
        self.write("README.md", readme([("one", "one"), ("one", "one")]))
        with self.assertRaises(ReferenceError) as context:
            validate_studies(self.studies)
        message = str(context.exception)
        self.assertIn("self-relations are not allowed", message)
        self.assertIn("duplicate relation", message)

    def test_duplicate_or_conflicting_relations_declarations_are_rejected(self) -> None:
        self.write("episodes/one.md", episode("one"))
        duplicate = readme([]).replace("relations: []", "relations: []\nrelations: []")
        self.write("README.md", duplicate)
        with self.assertRaisesRegex(ReferenceError, "multiple relations declarations"):
            validate_studies(self.studies)

        nested = readme([]).replace(
            "relations: []", "relations: []\n  - from: one\n    to: one"
        )
        self.write("README.md", nested)
        with self.assertRaisesRegex(ReferenceError, "cannot contain nested items"):
            validate_studies(self.studies)

        quoted = readme([]).replace(
            "relations: []", 'relations: []\n"relations":\n  - from: ghost\n    to: one'
        )
        self.write("README.md", quoted)
        with self.assertRaisesRegex(ReferenceError, "ASCII plain keys"):
            validate_studies(self.studies)

    def test_relation_fields_require_plain_separated_yaml(self) -> None:
        self.write("episodes/one.md", episode("one"))
        for name, source_line in {
            "compact field": "  - from:one\n    to: one",
            "quoted field": '  - "from": one\n    to: one',
            "unicode endpoint": "  - from: one\u00a0\n    to: one",
        }.items():
            with self.subTest(name=name):
                graph = (
                    "# Fixture study\n\n```yaml\nrelations:\n" + source_line + "\n```\n"
                )
                self.write("README.md", graph)
                with self.assertRaises(ReferenceError):
                    validate_studies(self.studies)

    def test_quoted_slug_values_and_crlf_are_supported(self) -> None:
        first = episode('"first"').replace("\n", "\r\n")
        second = episode("'second'", '"first"').replace("\n", "\r\n")
        graph = readme([("'first'", '"second"')]).replace("\n", "\r\n")
        self.write("episodes/one.md", first)
        self.write("episodes/two.md", second)
        self.write("README.md", graph)
        self.assertEqual(validate_studies(self.studies)["episodes"], 2)

    def test_yaml_looking_text_inside_an_outer_fence_is_ignored(self) -> None:
        disguised = (
            "# Fixture\n\n````text\n```yaml\nepisode_id: fake\n```\n````\n\n"
            + episode("real")
        )
        self.write("episodes/one.md", disguised)
        self.write("README.md", readme([]))
        self.assertEqual(validate_studies(self.studies)["episodes"], 1)

    def test_only_cr_and_lf_create_markdown_lines(self) -> None:
        pseudo_line_endings = {
            "vertical tab": "\v",
            "form feed": "\f",
            "file separator": "\x1c",
            "group separator": "\x1d",
            "record separator": "\x1e",
            "next line": "\u0085",
            "line separator": "\u2028",
            "paragraph separator": "\u2029",
        }
        self.write("README.md", readme([]))

        for name, separator in pseudo_line_endings.items():
            with self.subTest(name=name, placement="before LF"):
                disguised = f"# Fixture\n\n```yaml{separator}\nepisode_id: ghost\n```\n"
                self.write("episodes/one.md", disguised)
                with self.assertRaisesRegex(
                    ReferenceError, "missing fenced YAML episode metadata"
                ):
                    validate_studies(self.studies)

            with self.subTest(name=name, placement="inside physical line"):
                disguised = f"# Fixture\n\n```yaml{separator}episode_id: ghost\n```\n"
                self.write("episodes/one.md", disguised)
                with self.assertRaisesRegex(
                    ReferenceError, "missing fenced YAML episode metadata"
                ):
                    validate_studies(self.studies)

    def test_yaml_info_trims_only_gfm_ascii_whitespace(self) -> None:
        self.write("README.md", readme([]))
        for name, suffix in {
            "no-break space": "\u00a0",
            "em space": "\u2003",
            "byte-order mark": "\ufeff",
        }.items():
            with self.subTest(name=name):
                disguised = f"# Fixture\n\n```yaml{suffix}\nepisode_id: ghost\n```\n"
                self.write("episodes/one.md", disguised)
                with self.assertRaisesRegex(
                    ReferenceError, "missing fenced YAML episode metadata"
                ):
                    validate_studies(self.studies)

        spaced = episode("real").replace("```yaml\n", "``` \tyaml \t\n")
        self.write("episodes/one.md", spaced)
        self.assertEqual(validate_studies(self.studies)["episodes"], 1)

    def test_unclosed_yaml_fence_is_rejected(self) -> None:
        self.write("episodes/one.md", "# Fixture\n\n```yaml\nepisode_id: one\n")
        self.write("README.md", readme([]))
        with self.assertRaisesRegex(ReferenceError, "unclosed YAML fence"):
            validate_studies(self.studies)


if __name__ == "__main__":
    unittest.main()
