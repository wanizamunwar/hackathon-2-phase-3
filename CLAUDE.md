# Todo Full-Stack Web Application

## Project Overview
Phase II of the Evolution of Todo hackathon project. A multi-user full-stack web application with:
- **Backend**: Python FastAPI + SQLModel + Neon PostgreSQL
- **Frontend**: Next.js 16+ (App Router) + TypeScript + Tailwind CSS
- **Auth**: Better Auth (frontend) with JWT tokens verified by FastAPI (backend)

## Specs
- Feature spec: `specs/002-todo-fullstack-web/spec.md`
- Implementation plan: `specs/002-todo-fullstack-web/plan.md`
- Data model: `specs/002-todo-fullstack-web/data-model.md`
- Tasks: `specs/002-todo-fullstack-web/tasks.md`

## Dev Workflow
1. Backend runs on `http://localhost:8000` (FastAPI + uvicorn)
2. Frontend runs on `http://localhost:3000` (Next.js dev server)
3. Both share `BETTER_AUTH_SECRET` for JWT auth

## API Pattern
- All task endpoints: `/api/{user_id}/tasks[/{id}]`
- JWT token in `Authorization: Bearer <token>` header
- Backend verifies JWT and matches `user_id` from token with path parameter

## Key Conventions
- Spec-Driven Development: all code generated from specs
- No manual code writing — refine specs until output is correct
- Backend endpoints before frontend components
