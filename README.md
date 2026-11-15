# AI Integration Socmed API

Backend foundation for the Ruang Kita social-media and affiliate analytics project.

## Architecture

- **FastAPI** — API, orchestration, validation and business logic.
- **Supabase PostgreSQL** — central source of truth for accounts, posts, metrics and ingestion history.
- **Windsor.ai connector** — imports supported marketing and social analytics data.
- **Social platform connectors** — platform-specific publishing and insights integrations, added incrementally.
- **ChatGPT / analytics clients** — consume normalized data through the API.

```text
Windsor.ai / Social Platforms
            |
            v
       FastAPI API
   (connectors + services)
            |
            v
   Supabase PostgreSQL
            |
            v
   Analytics / ChatGPT
```

FastAPI owns integration logic and writes normalized records to PostgreSQL. Credentials stay server-side in environment variables. Never expose Supabase service-role credentials to a browser or public client.

## Repository layout

```text
app/
  api/routes/       HTTP endpoints
  core/             settings and Supabase client
  integrations/     external-system adapters
  services/         application/business logic
  schemas/          request/response models
tests/
```

## Local setup

1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in the values.
4. Run: `uvicorn app.main:app --reload`
5. Open `/docs` for interactive API documentation.

## Environment

- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY` (backend only; never commit or expose)
- `WINDSOR_API_KEY` (when Windsor connector is implemented)
- `API_KEY` (temporary internal API protection; replace with Supabase Auth/JWT validation before multi-user exposure)

## Initial implementation scope

This branch establishes the FastAPI application skeleton and integration boundaries. It does not yet create database tables, connect Windsor.ai, or publish to social platforms. Those will be implemented and verified as separate steps.
