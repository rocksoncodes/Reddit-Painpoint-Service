# Reddit-Problem-Discovery-Service (Reddit-only)

This repository implements a backend-first AI agent that discovers recurring problems and sentiment signals in niche Reddit communities. The project is intentionally focused on Reddit as the single input source; other platforms are out of scope for now.

Quick summary:
- Input: Reddit posts & comments (via Reddit API)
- Process: Text cleaning, sentiment scoring, LLM-based validation (Gemini client)
- Output: Structured briefs stored in the local database, optional Notion sync (under review), and email delivery

- Collect posts and comments exclusively from configured subreddits.
## Why Reddit-only?
Focusing on one platform keeps ingestion, privacy and evaluation requirements simple and makes prompts and data pipelines more effective for the kinds of conversational structure Reddit provides (posts + nested comments). If you later want other platforms, treat them as another "Input" provider and implement a matching client + ingress service.

- Basic LLM integration for validation prompts (Gemini/Google LLM; optional)
## Problem
Manual discovery of recurring, real-world problems across subreddits is slow and noisy. This service automates discovery, validation, and packaging of those findings so teams can act faster.
- Modular code structure with agents, services and pipelines
<img width="1832" height="967" alt="image" src="https://github.com/user-attachments/assets/334da5c1-31af-4c92-85b0-3930b28cc464" />
## Solution (what this repo provides)
- Periodic collection of posts and comments from configured subreddits.
- Processing pipelines to filter, summarize and analyze sentiment.
- LLM-based (Gemini) checks to validate whether a detected issue is a meaningful problem.
- Outputs: curated briefs are persisted to the local DB and can be emailed or (optionally) synced to Notion.
# Quick start
### Prerequisites
## Tech stack
Python 3.11+ (tested with 3.13)
A Reddit app (client ID & secret)
- Gemini (Google LLM) client (thin wrapper in `clients/`)
- SQLAlchemy (models + engine in `database/`)
- Jinja2 templates for egress email rendering (`utils/templates/card.html`)
- SMTP (Gmail example in `services/egress/egress_service.py`)
- Structured logging via `utils/logger.py`


## Key features
    git clone https://github.com/[your-username]/Market-Scouting-AI-Agent.git
   ```

### 2. Create a virtual environment and install dependencies

```bash
    python -m venv .venv
    .\.venv\Scripts\activate    # Windows
## Project organization (Input / Process / Output)
The repository is easiest to reason about when viewed as three layers: Input (acquisition), Process (analysis), and Output (delivery). Below is the mapping to the current folders and files so you can find the code quickly.
```

  - `clients/reddit_client.py` — low-level Reddit API wrapper
  - `services/ingress/` — higher-level ingestion logic & Reddit-specific services
  - `engines/ingress.py` — runnable ingest engine
```

  - `pipelines/` — processing and sentiment pipelines (`sentiment_pipeline.py`, etc.)
  - `services/core/` — core business logic and LLM validation (`core_service.py`, `sentiment_service.py`)
  - `engines/core.py` — orchestrates processing runs
    ```bash
       python engines\ingest_engine.py
  - `services/egress/` — email/Notion/sink logic (`egress_service.py`, `storage_service.py`)
  - `engines/egress.py` — runnable egress engine
  - `database/` — where processed briefs are persisted
  - `emails/` + `utils/templates/` — email templates and rendering assets


## Recommended alternative folder names
If you prefer explicit layer names instead of `ingress/core/egress`, here are options ranked by clarity and common usage:
# Configuration (.env)
- Simple nouns (explicit):
  - `input/`  (or `ingest/`)
  - `process/` (or `analyze/`, `transform/`)
  - `output/` (or `deliver/`, `publish/`)

- More domain-oriented:
  - `acquisition/` — `analysis/` — `delivery/`

Notes on renaming: renaming folders is a breaking change for imports. If you do rename them, either update imports across the project or add small package shim modules that re-export the previous paths to preserve compatibility.


## Environment variables
The following environment variables are used by the project (add any others required by your integrations):

``` bash
REDDIT_CLIENT_ID       # Reddit API client ID
REDDIT_CLIENT_SECRET   # Reddit API secret
REDDIT_USER_AGENT      # Reddit API user agent string
GEMINI_API_KEY         # Gemini / Google LLM API key (optional)
Optional / output-related:
NOTION_DB_ID           # (optional) Notion database id
```

Notes:
```bash
Keep secrets out of version control. Use a secrets manager for production.
```

# Project structure (overview)
## How to run (quick start — Windows example)
- clients/        thin API clients (Reddit, Gemini)
- engines/        runnable scripts / entrypoints (reddit_ingest, curator)
- services/       business logic and integrations (scrapers, storage)
- pipelines/      data processing pipelines (sentiment, curator)
- database/       SQLAlchemy models and DB initialization
- utils/          shared helpers

# Development status

Branch: MSAA-05-Curator-Agent-Development

- ✅ Project skeleton and core modules
- ✅ Reddit ingestion and basic data collection
- ✅ Gemini integration for evaluation
3. Run a specific engine (example: ingress)
- 📝 Planned: Notion sync, richer problem-ranking, Email notifications


# or run processing/evaluation
# Contributing
# or send egress outputs

Contributions and PRs are welcome. Suggested ways to help:
- Implement planned features from the roadmap
- Improve data processing and validation prompts
## Notes & current limitations (explicit)
- Improve documentation and examples

When opening a PR, include tests or a short demo showing the change.
