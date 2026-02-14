import unittest

from app.engine import generate_analysis
from app.schemas import AnalysisMode, AnalysisRequest


class EngineTests(unittest.TestCase):
    def test_probabilities_sum_to_one_quant_mode(self) -> None:
        response = generate_analysis(
            AnalysisRequest(query="Gold ETF", mode=AnalysisMode.QUANT)
        )
        probs = response.directional_probability
        total = probs.bullish + probs.neutral + probs.bearish
        self.assertAlmostEqual(total, 1.0)

    def test_mode_biases_are_distinct(self) -> None:
        quant = generate_analysis(
            AnalysisRequest(query="SPY", mode=AnalysisMode.QUANT)
        ).directional_probability
        buffett = generate_analysis(
            AnalysisRequest(query="SPY", mode=AnalysisMode.BUFFETT)
        ).directional_probability
        dalio = generate_analysis(
            AnalysisRequest(query="SPY", mode=AnalysisMode.DALIO)
        ).directional_probability

        self.assertNotEqual((quant.bullish, quant.neutral, quant.bearish), (buffett.bullish, buffett.neutral, buffett.bearish))
        self.assertNotEqual((quant.bullish, quant.neutral, quant.bearish), (dalio.bullish, dalio.neutral, dalio.bearish))

    def test_attribution_weights_sum_to_one(self) -> None:
        response = generate_analysis(
            AnalysisRequest(query="QQQ", mode=AnalysisMode.QUANT)
        )
        total_weight = sum(item.weight for item in response.signal_attribution)
        self.assertAlmostEqual(total_weight, 1.0)


if __name__ == "__main__":
    unittest.main()
