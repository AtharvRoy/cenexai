from fastapi import FastAPI

from app.engine import generate_analysis
from app.schemas import AnalysisRequest, AnalysisResponse

app = FastAPI(
    title="Cenex AI API",
    description="MVP market intelligence API scaffold for Cenex AI.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest) -> AnalysisResponse:
    return generate_analysis(request)
