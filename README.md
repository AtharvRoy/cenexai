# Cenex AI

Institutional-grade AI market intelligence for probabilistic, explainable decision support.

## Vision

Cenex AI is designed to become an **AI-native financial research terminal** that synthesizes market, macro, news, and fundamental signals into structured forecasts. The product focus is not "trading bot signals," but an institutional-style **thinking engine** for investors and analysts.

## Problem

Modern investors face fragmented workflows and low decision clarity:
- Information overload
- Disconnected tools (charts, news, fundamentals, macro)
- Limited explainability in AI outputs
- Emotion-driven decisions under uncertainty

## Solution

Cenex AI combines multi-modal data and multi-agent reasoning to deliver:
- Directional probabilities (not binary predictions)
- Explainable signal attribution
- Risk-aware scenario breakdowns
- Actionable, institutional-style research outputs

## Target Users

### Primary
- Quantitative traders
- Portfolio managers
- Hedge fund analysts
- Independent investors seeking institutional-grade insights

### Secondary
- Financial educators
- AI researchers
- Macro strategists

## Core Product Objectives

- Deliver explainable market forecasts
- Reduce analysis time by up to 90%
- Improve risk-awareness in decision workflows
- Enable macro + micro signal synthesis

### KPI Framework
- Prediction performance vs baseline models
- User retention and engagement depth
- Probability calibration quality
- Signal quality proxy (e.g., Sharpe-oriented metrics)

## Core Features

### 1) Multi-Modal Market Intelligence Engine
**Inputs:**
- OHLCV market data
- Technical indicators
- Macro variables
- News sentiment and narratives
- Earnings and filings

**Outputs:**
- Market directional probabilities
- Key risk factors
- Strategy suggestions

### 2) Analysis Modes
- **Buffett Mode:** value-oriented interpretation
- **Dalio Mode:** macro-cycle perspective
- **Quant Mode:** statistical and systematic framing

### 3) Explainable AI Layer
Each prediction includes:
- Signal attribution
- Confidence and calibration context
- Conflicting indicator analysis
- Scenario decomposition

### 4) News Intelligence Agent
- Sentiment shift detection
- Narrative extraction and tracking
- Event-to-price linkage analysis

### 5) Portfolio Advisor (Phase 2)
- Allocation guidance
- Risk concentration alerts
- Correlation-aware analysis

## UX Flow

1. User query (example: `Analyze Gold ETF`)
2. System processes market + macro + news + risk signals
3. Output returns structured institutional analysis:
   - Directional probabilities
   - Risk context
   - Strategy ideas

## System Architecture

### Layer 1: Data Ingestion
- Market APIs (e.g., Polygon, Alpaca, Binance)
- Macro feeds (e.g., FRED)
- News and filings (RSS, SEC, etc.)

Pipeline:
`Raw -> Normalize -> Timestamp Sync -> Storage`

### Layer 2: Feature Engineering
- Technical indicators
- Volatility / regime features
- NLP embeddings for unstructured text

### Layer 3: Multi-Agent Intelligence
- **Quant Agent:** forecasting, momentum, regime detection
- **News Agent:** sentiment, events, narrative scoring
- **Risk Agent:** drawdown/volatility/correlation shifts
- **Meta Agent:** probabilistic ensemble output

### Layer 4: Explainability Engine
- Feature importance
- Reasoning summary
- Signal conflict identification

### Layer 5: Interface Layer
- Conversational research interface
- Dashboard visualizations
- Structured report views

## Recommended Tech Stack

- **Backend:** Python, FastAPI
- **Data:** Pandas, Polars, Arrow
- **Models:** LightGBM, XGBoost, time-series transformers
- **NLP:** LLM + embeddings
- **Vector DB:** Pinecone or Weaviate
- **Infra:** Docker, AWS S3/Lambda, Kubernetes (later)
- **Frontend:** Next.js, Tailwind CSS, Recharts/TradingView components

## Competitive Positioning

### Competitors
- Bloomberg Terminal
- Kensho
- AlphaSense
- TradingView

### Cenex AI Advantage
- Explainable probabilistic forecasts
- Multi-agent synthesis architecture
- Retail-accessible institutional intelligence

## Business Model

- Subscription tiers ($29-$99 range for Pro tiers)
- Quant/Research API access
- Institutional licensing and white-label options
- Research-as-a-service offerings

## Product Roadmap

### Phase 1 (MVP)
- Data ingestion pipeline
- Baseline prediction engine
- Structured report interface

### Phase 2 (Intelligence Layer)
- News NLP agent
- Explainability module
- Portfolio analytics

### Phase 3 (Institutional Grade)
- Real-time streaming signals
- Backtesting engine
- Full multi-agent orchestration

## Risks and Mitigations

- **Model overfitting** -> walk-forward validation and robust evaluation
- **Data quality drift** -> source monitoring and validation checks
- **Regulatory expectations** -> transparent disclosures and controls
- **User overconfidence in AI** -> explicit confidence and uncertainty framing

## Long-Term Vision

Cenex AI evolves from:
1. Research assistant
2. Decision intelligence engine
3. Institutional platform
4. Autonomous AI research network

The strategic moat is built through **data infrastructure + feedback loops + workflow integration**, not model novelty alone.

## MVP API Scaffold (Next Step)

This repository now includes a minimal FastAPI backend scaffold to make the PRD executable.

### Endpoints
- `GET /health` -> service health check
- `POST /analyze` -> returns structured probabilistic market analysis in Buffett/Dalio/Quant mode

### Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open API docs at `http://127.0.0.1:8000/docs`.

### Basic Validation

```bash
python -m compileall app tests
python -m unittest discover -s tests -p 'test_*.py'
```


### One-command setup (recommended)

Linux/macOS:

```bash
./scripts/bootstrap.sh
```

Windows PowerShell:

```powershell
./scripts/bootstrap.ps1
```

### Makefile shortcuts

```bash
make doctor    # preflight environment checks
make install   # create venv + install deps
make test      # run unit tests
make run       # start API
```

### Environment diagnostics

Run a quick preflight to identify missing deps/network issues before setup:

```bash
make doctor
# or
python scripts/doctor.py
```


### Troubleshooting

If installation fails with proxy/network errors, your environment may block pip index access.
In that case run the same commands on your local machine or configure pip proxy/index settings,
then re-run:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p 'test_*.py'
```
