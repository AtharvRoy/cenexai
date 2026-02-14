from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class AnalysisMode(str, Enum):
    BUFFETT = "buffett"
    DALIO = "dalio"
    QUANT = "quant"


class AnalysisRequest(BaseModel):
    query: str = Field(..., min_length=2, description="Instrument or market query")
    mode: AnalysisMode = Field(default=AnalysisMode.QUANT)


class DirectionalProbability(BaseModel):
    bullish: float = Field(..., ge=0.0, le=1.0)
    neutral: float = Field(..., ge=0.0, le=1.0)
    bearish: float = Field(..., ge=0.0, le=1.0)


class SignalAttribution(BaseModel):
    signal: str
    weight: float = Field(..., ge=0.0, le=1.0)
    rationale: str


class Scenario(BaseModel):
    name: str
    probability: float = Field(..., ge=0.0, le=1.0)
    implication: str


class AnalysisResponse(BaseModel):
    instrument: str
    mode: AnalysisMode
    directional_probability: DirectionalProbability
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    key_risk_factors: List[str]
    signal_attribution: List[SignalAttribution]
    conflicting_indicators: List[str]
    scenarios: List[Scenario]
    strategy_suggestions: List[str]
