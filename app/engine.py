from app.schemas import (
    AnalysisMode,
    AnalysisRequest,
    AnalysisResponse,
    DirectionalProbability,
    Scenario,
    SignalAttribution,
)


def _mode_bias(mode: AnalysisMode) -> tuple[float, float, float]:
    if mode == AnalysisMode.BUFFETT:
        return (0.45, 0.35, 0.20)
    if mode == AnalysisMode.DALIO:
        return (0.35, 0.40, 0.25)
    return (0.50, 0.30, 0.20)


def generate_analysis(request: AnalysisRequest) -> AnalysisResponse:
    bullish, neutral, bearish = _mode_bias(request.mode)

    attributions = [
        SignalAttribution(
            signal="Technical momentum",
            weight=0.35,
            rationale="Price trend remains above medium-term baseline.",
        ),
        SignalAttribution(
            signal="Macro regime",
            weight=0.30,
            rationale="Growth and liquidity conditions are mixed but stable.",
        ),
        SignalAttribution(
            signal="News sentiment",
            weight=0.20,
            rationale="Recent narrative flow is slightly constructive.",
        ),
        SignalAttribution(
            signal="Risk conditions",
            weight=0.15,
            rationale="Volatility has cooled but tail-risk remains elevated.",
        ),
    ]

    return AnalysisResponse(
        instrument=request.query,
        mode=request.mode,
        directional_probability=DirectionalProbability(
            bullish=bullish,
            neutral=neutral,
            bearish=bearish,
        ),
        confidence_score=0.69,
        key_risk_factors=[
            "Macro surprise risk (inflation / rates)",
            "Event-driven gap risk from headlines",
            "Cross-asset correlation spikes",
        ],
        signal_attribution=attributions,
        conflicting_indicators=[
            "Constructive momentum vs fragile macro breadth",
            "Positive narrative flow vs cautious positioning",
        ],
        scenarios=[
            Scenario(
                name="Base case",
                probability=0.55,
                implication="Range-up drift with moderate volatility.",
            ),
            Scenario(
                name="Risk-off drawdown",
                probability=0.25,
                implication="Short, sharp downside if macro surprise hits.",
            ),
            Scenario(
                name="Breakout continuation",
                probability=0.20,
                implication="Sustained trend extension on supportive catalysts.",
            ),
        ],
        strategy_suggestions=[
            "Favor risk-defined entries over directional leverage.",
            "Scale exposure on confirmation rather than anticipation.",
            "Monitor macro event calendar for regime shifts.",
        ],
    )
