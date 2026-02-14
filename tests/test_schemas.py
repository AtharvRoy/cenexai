import unittest

from pydantic import ValidationError

from app.schemas import AnalysisMode, AnalysisRequest


class SchemaTests(unittest.TestCase):
    def test_request_defaults_to_quant_mode(self) -> None:
        request = AnalysisRequest(query="BTC")
        self.assertEqual(request.mode, AnalysisMode.QUANT)

    def test_query_min_length_validation(self) -> None:
        with self.assertRaises(ValidationError):
            AnalysisRequest(query="A")


if __name__ == "__main__":
    unittest.main()
