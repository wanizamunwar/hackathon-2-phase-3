# Implementation Plan: Todo Full-Stack Web Application

**Branch**: `002-todo-fullstack-web` | **Date**: 2026-02-09 | **Spec**: `specs/002-todo-fullstack-web/spec.md`
**Input**: Feature specification from `/specs/002-todo-fullstack-web/spec.md`

## Summary

Transform the Phase I in-memory Python console todo app into a multi-user full-stack web application. The backend is a Python FastAPI server using SQLModel ORM connected to Neon Serverless PostgreSQL. The frontend is a Next.js 16+ (App Router) application with TypeScript and Tailwind CSS. Authentication is handled by Better Auth on the frontend, issuing JWT tokens that the FastAPI backend verifies for user isolation. Features include full CRUD, priorities/tags, search/filter, and sort.

## Technical Context

**Language/Version**: Python 3.12+ (backend), TypeScript 5+ (frontend)
**Primary Dependencies**: FastAPI, SQLModel, uvicorn, python-jose, Next.js 16+, Better Auth, Tailwind CSS
**Storage**: Neon Serverless PostgreSQL
**Testing**: pytest (backend), manual E2E testing (frontend)
**Target Platform**: Web (desktop + mobile responsive)
**Project Type**: web (frontend + backend monorepo)
**Performance Goals**: < 500ms API response time, smooth UI interactions
**Constraints**: JWT-based stateless auth, user isolation on every endpoint, shared BETTER_AUTH_SECRET
**Scale/Scope**: Multi-user, 100s of tasks per user, 2 services (frontend + backend)

## Constitution Check

*GATE: Must pass before implementation.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Spec-Driven Development | PASS | Spec written before implementation |
| II. Pythonic Design | PASS | Backend follows PEP 8, uses FastAPI + SQLModel |
| III. Test-Driven Development | PASS | pytest for backend API tests |
| IV. Web Application Interface | PASS | Replaces console-first with web-first (Phase II evolution) |
| V. Persistent Data Management | PASS | Neon PostgreSQL replaces in-memory storage (Phase II evolution) |
| VI. Modularity and Simplicity | PASS | Separated frontend/backend, clear API boundaries |

### Development Constraints
- **Technology Stack**: Python FastAPI (backend) + Next.js TypeScript (frontend) | PASS
- **Code Generation**: All code via Claude Code + Spec-Kit Plus | PASS
- **Data Persistence**: Neon Serverless PostgreSQL via SQLModel | PASS

### Quality Gates
- Automated testing for backend API endpoints | PASS
- Functional verification through browser interaction | PASS
- User isolation verification | PASS

## Project Structure

### Documentation (this feature)

```text
specs/002-todo-fullstack-web/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file
├── research.md          # Technical decisions
├── data-model.md        # Task & User entity models
├── quickstart.md        # Setup & running guide
├── contracts/           # API contracts
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
backend/
├── main.py              # FastAPI app entry point
├── db.py                # Neon database connection + session
├── models.py            # SQLModel database models (Task)
├── auth.py              # JWT verification middleware
├── routes/
│   └── tasks.py         # Task CRUD API route handlers
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── tests/
    └── test_tasks.py    # API endpoint tests

frontend/
├── package.json         # Node.js dependencies
├── next.config.ts       # Next.js configuration
├── tailwind.config.ts   # Tailwind CSS configuration
├── tsconfig.json        # TypeScript configuration
├── .env.example         # Environment variable template
├── src/
│   ├── app/
│   │   ├── layout.tsx           # Root layout
│   │   ├── page.tsx             # Landing/redirect page
│   │   ├── (auth)/
│   │   │   ├── signin/page.tsx  # Sign in page
│   │   │   └── signup/page.tsx  # Sign up page
│   │   └── dashboard/
│   │       └── page.tsx         # Task dashboard (main app)
│   ├── components/
│   │   ├── TaskList.tsx         # Task list display
│   │   ├── TaskItem.tsx         # Individual task card
│   │   ├── TaskForm.tsx         # Create/edit task form
│   │   ├── SearchFilter.tsx     # Search bar + filter controls
│   │   ├── SortControls.tsx     # Sort options
│   │   └── AuthForm.tsx         # Signin/signup form
│   ├── lib/
│   │   ├── api.ts               # Backend API client
│   │   ├── auth.ts              # Better Auth client config
│   │   └── auth-server.ts       # Better Auth server config
│   └── middleware.ts            # Auth middleware (route protection)
└── CLAUDE.md

CLAUDE.md                # Root Claude Code instructions
docker-compose.yml       # Run both services together
.env.example             # Root env template
```

**Structure Decision**: Web application structure (Option 2) — separate `frontend/` and `backend/` directories in a monorepo. Phase I console app code is preserved in `src/` directory. The backend uses FastAPI with SQLModel for clean Python API development. The frontend uses Next.js App Router for modern React patterns.

## Complexity Tracking

No constitution violations. Structure follows standard web app monorepo pattern.
