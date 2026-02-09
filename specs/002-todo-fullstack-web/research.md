# Research: Todo Full-Stack Web Application

## Overview

Phase II transforms the Phase I in-memory console app into a full-stack web application. This document captures the key technical decisions made for the implementation.

---

## 1. Backend Framework: FastAPI

**Decision**: Use FastAPI as the Python backend framework.

**Rationale**:
- Required by hackathon technology stack
- Async-first, high performance
- Built-in OpenAPI/Swagger documentation
- Native Pydantic integration for request/response validation
- SQLModel (built on Pydantic + SQLAlchemy) integrates seamlessly

**Alternatives considered**: Django REST Framework (heavier, not required), Flask (less modern async support)

---

## 2. ORM: SQLModel

**Decision**: Use SQLModel for database interaction.

**Rationale**:
- Required by hackathon technology stack
- Combines SQLAlchemy ORM with Pydantic validation
- Single model class serves as both database model and API schema
- Built by the same author as FastAPI (Sebastian Ramirez)

**Alternatives considered**: SQLAlchemy directly (more boilerplate), Tortoise ORM (less ecosystem support)

---

## 3. Database: Neon Serverless PostgreSQL

**Decision**: Use Neon as the PostgreSQL provider.

**Rationale**:
- Required by hackathon technology stack
- Serverless — no infrastructure management
- PostgreSQL compatible — standard SQL, JSON support for tags
- Free tier available for development
- Connection via standard PostgreSQL connection string

**Connection**: Use `DATABASE_URL` environment variable with `postgresql+psycopg2://` or `postgresql+asyncpg://` scheme.

---

## 4. Frontend Framework: Next.js 16+ (App Router)

**Decision**: Use Next.js with App Router for the frontend.

**Rationale**:
- Required by hackathon technology stack
- App Router provides modern React Server Components
- Built-in routing, layouts, and middleware
- TypeScript support out of the box
- Tailwind CSS integration via official template

---

## 5. Authentication: Better Auth with JWT

**Decision**: Use Better Auth on the frontend with JWT tokens for backend verification.

**Rationale**:
- Required by hackathon technology stack
- Better Auth runs on the Next.js server, managing user signup/signin
- JWT plugin allows issuing tokens that the FastAPI backend can verify independently
- Shared `BETTER_AUTH_SECRET` enables stateless cross-service auth
- No shared database session required between frontend and backend

**How it works**:
1. User signs up/in via Better Auth on the Next.js frontend
2. Better Auth issues a JWT token containing user_id, email
3. Frontend attaches JWT to every API request as `Authorization: Bearer <token>`
4. FastAPI backend verifies JWT signature using the shared secret
5. Backend extracts user_id from token and filters data accordingly

---

## 6. Tags Storage: JSON Column

**Decision**: Store tags as a JSON array in PostgreSQL.

**Rationale**:
- PostgreSQL has native JSON/JSONB support
- Simpler than a separate tags table with many-to-many relationship
- Sufficient for the scale of this application (user-defined labels)
- SQLModel supports JSON columns via SQLAlchemy's `Column(JSON)`

**Alternatives considered**: Separate `tags` table with many-to-many join (over-engineered for this use case)

---

## 7. Project Structure: Monorepo

**Decision**: Use a monorepo with `frontend/` and `backend/` directories.

**Rationale**:
- Required by hackathon monorepo organization guide
- Single repository for spec-driven development workflow
- Claude Code can reference specs and implement across both services
- Phase I console app code preserved in `src/` directory
- docker-compose.yml at root for running both services

---

## 8. API Design: RESTful with User ID in Path

**Decision**: Use `/api/{user_id}/tasks` pattern for API endpoints.

**Rationale**:
- Required by hackathon API specification
- User ID in path makes ownership explicit
- Backend validates that JWT user_id matches path user_id
- Standard REST conventions for CRUD operations
