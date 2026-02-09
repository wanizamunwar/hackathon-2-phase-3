# Backend — FastAPI

## Tech Stack
- Python 3.12+, FastAPI, SQLModel, uvicorn
- Neon Serverless PostgreSQL via psycopg2-binary
- JWT verification via python-jose

## Patterns
- **Models**: SQLModel classes in `models.py` (both DB model and Pydantic schema)
- **Routes**: Organized in `routes/` directory, included via `app.include_router()`
- **Auth**: JWT middleware in `auth.py` — `get_current_user()` dependency extracts user_id
- **DB**: Session dependency in `db.py` — `get_session()` yields SQLModel sessions
- **Entry point**: `main.py` — FastAPI app with CORS, router inclusion, startup events

## Conventions
- Use `Depends()` for dependency injection (auth, db session)
- Validate user_id from JWT matches path parameter on every request
- Return appropriate HTTP status codes (200, 201, 400, 401, 403, 404)
- Use SQLModel `Field()` for validation constraints

## Running
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
