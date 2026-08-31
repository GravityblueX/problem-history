from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_problem_episodes import (  # noqa: E402
    ContractError,
    discover_json,
    validate_documents,
)


SCHEMA = REPO_ROOT / "schemas" / "problem-episode.schema.json"
FIXTURES = REPO_ROOT / "fixtures" / "problem-episodes"


class ProblemEpisodeContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture_paths = discover_json([FIXTURES])
        cls.documents = [
            json.loads(path.read_text(encoding="utf-8")) for path in cls.fixture_paths
        ]

    def _validate_mutation(self, documents: list[dict]) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths: list[Path] = []
            for index, document in enumerate(documents):
                path = root / f"fixture-{index}.json"
                path.write_text(
                    json.dumps(document, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                paths.append(path)
            validate_documents(SCHEMA, paths)

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_all_fixtures_validate_as_one_corpus(self) -> None:
        counts = validate_documents(SCHEMA, self.fixture_paths)
        self.assertEqual(counts["documents"], 3)
        self.assertEqual(counts["relations"], 2)

    def test_fixture_suite_exercises_all_formulation_sources(self) -> None:
        represented = {
            formulation["source_type"]
            for document in self.documents
            for formulation in document["formulations"]
        }
        self.assertEqual(
            represented,
            {"actor_explicit", "actor_reconstructed", "researcher_analytic"},
        )

    def test_reconstructed_formulation_requires_an_audit_trail(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[1]["formulations"][0].pop("reconstruction_note")
        with self.assertRaisesRegex(ContractError, "reconstruction_note"):
            self._validate_mutation(documents)

        documents = copy.deepcopy(self.documents)
        documents[1]["formulations"][0]["evidence_ids"] = [
            "control-engineer-request"
        ]
        with self.assertRaises(ContractError):
            self._validate_mutation(documents)

    def test_actor_formulation_requires_an_actor(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["formulations"][0]["actor_ids"] = []
        with self.assertRaises(ContractError):
            self._validate_mutation(documents)

    def test_unretrievable_source_requires_an_explanation(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["sources"][0].pop("notes")
        with self.assertRaisesRegex(ContractError, "notes"):
            self._validate_mutation(documents)

    def test_relation_requires_continuity_and_discontinuity_evidence(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["relations"][0]["discontinuity_evidence"] = []
        with self.assertRaises(ContractError):
            self._validate_mutation(documents)

    def test_unresolved_evidence_reference_is_rejected(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["stakes"][0]["evidence_ids"] = ["missing-evidence"]
        with self.assertRaisesRegex(ContractError, "unresolved evidence"):
            self._validate_mutation(documents)

    def test_unresolved_relation_target_is_rejected(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["relations"][0]["target_episode_id"] = "missing-episode"
        with self.assertRaisesRegex(ContractError, "unresolved episode"):
            self._validate_mutation(documents)

    def test_non_relation_cross_episode_evidence_is_rejected(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["stakes"][0]["evidence_ids"] = ["control-question"]
        with self.assertRaisesRegex(ContractError, "non-relation field references"):
            self._validate_mutation(documents)

    def test_relation_source_must_match_container(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["relations"][0]["source_episode_id"] = documents[1][
            "episode_id"
        ]
        with self.assertRaisesRegex(ContractError, "must equal the containing"):
            self._validate_mutation(documents)

    def test_reversed_period_is_rejected(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["period"]["start_year"] = 1882
        documents[0]["period"]["end_year"] = 1881
        with self.assertRaisesRegex(ContractError, "start_year must not exceed"):
            self._validate_mutation(documents)

    def test_unknown_field_is_rejected_by_strict_schema(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["modern_summary"] = "This field bypasses the evidence model."
        with self.assertRaisesRegex(ContractError, "Additional properties"):
            self._validate_mutation(documents)

    def test_malformed_structure_returns_contract_error(self) -> None:
        documents = copy.deepcopy(self.documents)
        documents[0]["actors"] = {"not": "an array"}
        with self.assertRaisesRegex(ContractError, "is not of type 'array'"):
            self._validate_mutation(documents)


if __name__ == "__main__":
    unittest.main()
