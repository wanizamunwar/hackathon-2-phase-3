# Tasks: Todo Full-Stack Web Application

**Input**: Design documents from `/specs/002-todo-fullstack-web/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Monorepo structure, project initialization, dependencies

- [X] T001 Create monorepo directory structure: `backend/`, `backend/routes/`, `backend/tests/`, `frontend/`
- [X] T002 [P] Create root `CLAUDE.md` with project overview, spec references, and dev workflow
- [X] T003 [P] Create `backend/CLAUDE.md` with FastAPI patterns and conventions
- [X] T004 [P] Create `frontend/CLAUDE.md` with Next.js patterns and conventions
- [X] T005 [P] Create `backend/requirements.txt` with dependencies: fastapi, uvicorn, sqlmodel, python-jose[cryptography], psycopg2-binary, python-dotenv
- [X] T006 [P] Create `backend/.env.example` with DATABASE_URL and BETTER_AUTH_SECRET placeholders
- [X] T007 [P] Create `frontend/.env.example` with BETTER_AUTH_SECRET, NEXT_PUBLIC_API_URL, BETTER_AUTH_URL placeholders
- [X] T008 Initialize Next.js 16+ project in `frontend/` with TypeScript, Tailwind CSS, App Router
- [X] T009 [P] Create root `.env.example` with all environment variable references
- [X] T010 [P] Create `docker-compose.yml` for running both services together

**Checkpoint**: Monorepo structure ready, both projects initialized with dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Database connection, models, auth middleware — MUST be complete before ANY user story

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T011 Create database connection module: `backend/db.py` — Neon PostgreSQL engine, session dependency, table creation
- [X] T012 Create Task SQLModel: `backend/models.py` — Task entity with all fields (id, user_id, title, description, completed, priority, tags, created_at, updated_at)
- [X] T013 Create JWT verification middleware: `backend/auth.py` — decode/verify JWT from Authorization header, extract user_id, dependency for routes
- [X] T014 Create FastAPI app entry point: `backend/main.py` — app instance, CORS middleware, router inclusion, startup event for table creation
- [X] T015 [P] Create Better Auth server configuration: `frontend/src/lib/auth-server.ts` — Better Auth instance with JWT plugin, email/password provider
- [X] T016 [P] Create Better Auth client configuration: `frontend/src/lib/auth.ts` — client-side auth helpers (signIn, signUp, signOut, useSession)
- [X] T017 Create API client module: `frontend/src/lib/api.ts` — fetch wrapper that attaches JWT token to all requests, base URL config
- [X] T018 Create Next.js auth middleware: `frontend/src/middleware.ts` — protect /dashboard routes, redirect unauthenticated users to /signin
- [X] T019 Create root layout: `frontend/src/app/layout.tsx` — HTML shell, Tailwind setup, auth session provider

**Checkpoint**: Foundation ready — database connected, models defined, auth middleware in place, API client configured

---

## Phase 3: User Story 1 — User Registration & Authentication (Priority: P1)

**Goal**: Users can sign up, sign in, and log out. Sessions are managed via Better Auth with JWT tokens.

**Independent Test**: Navigate to app → sign up → log out → sign in → verify dashboard access

### Implementation for User Story 1

- [X] T020 [US1] Create signup page: `frontend/src/app/(auth)/signup/page.tsx` — email, name, password form, Better Auth signUp call, redirect to dashboard
- [X] T021 [US1] Create signin page: `frontend/src/app/(auth)/signin/page.tsx` — email, password form, Better Auth signIn call, redirect to dashboard
- [X] T022 [P] [US1] Create AuthForm component: `frontend/src/components/AuthForm.tsx` — reusable form for signin/signup with validation, error display
- [X] T023 [US1] Create landing page: `frontend/src/app/page.tsx` — redirect to /dashboard if authenticated, else to /signin
- [X] T024 [US1] Create Better Auth API route handler: `frontend/src/app/api/auth/[...all]/route.ts` — catch-all route for Better Auth endpoints
- [X] T025 [US1] Add logout button to dashboard layout with signOut functionality

**Checkpoint**: User can sign up, sign in, log out. Unauthenticated users are redirected to signin.

---

## Phase 4: User Story 2 — Add a New Task (Priority: P1)

**Goal**: Authenticated users can create tasks with title, description. Tasks are persisted in Neon DB.

**Independent Test**: Sign in → click Add Task → enter title → submit → verify task appears in list

### Implementation for User Story 2

- [X] T026 [US2] Create task CRUD routes: `backend/routes/tasks.py` — POST /api/{user_id}/tasks endpoint with JWT auth dependency, input validation, task creation
- [X] T027 [US2] Register task router in `backend/main.py`
- [X] T028 [US2] Create TaskForm component: `frontend/src/components/TaskForm.tsx` — title (required), description (optional) fields, submit handler, validation
- [X] T029 [US2] Create dashboard page: `frontend/src/app/dashboard/page.tsx` — layout with TaskForm and TaskList, fetch user tasks on load
- [X] T030 [US2] Wire TaskForm to API client POST call in `frontend/src/lib/api.ts`

**Checkpoint**: User can create tasks that persist in the database and appear in the task list.

---

## Phase 5: User Story 3 — View All Tasks (Priority: P1)

**Goal**: Authenticated users see all their tasks in a list. Empty state shown when no tasks exist.

**Independent Test**: Sign in with user who has tasks → verify all tasks displayed with title, status, date

### Implementation for User Story 3

- [X] T031 [US3] Create GET /api/{user_id}/tasks endpoint in `backend/routes/tasks.py` — return all tasks for authenticated user, filtered by user_id
- [X] T032 [US3] Create GET /api/{user_id}/tasks/{id} endpoint in `backend/routes/tasks.py` — return single task details
- [X] T033 [US3] Create TaskList component: `frontend/src/components/TaskList.tsx` — display tasks with title, status, priority badge, created date, empty state
- [X] T034 [US3] Create TaskItem component: `frontend/src/components/TaskItem.tsx` — individual task card with visual indicators
- [X] T035 [US3] Wire TaskList to API client GET call in dashboard page

**Checkpoint**: User can view all their tasks. Empty state shown for new users. Other users' tasks are not visible.

---

## Phase 6: User Story 4 — Update a Task (Priority: P2)

**Goal**: Users can edit task title and description of existing tasks.

**Independent Test**: Sign in → select task → edit title → save → verify changes persist

### Implementation for User Story 4

- [X] T036 [US4] Create PUT /api/{user_id}/tasks/{id} endpoint in `backend/routes/tasks.py` — update task fields, validate ownership, refresh updated_at
- [X] T037 [US4] Add edit mode to TaskItem component or create edit modal in `frontend/src/components/TaskForm.tsx`
- [X] T038 [US4] Wire edit form to API client PUT call, refresh task list after update

**Checkpoint**: User can edit task details. Changes persist and updated_at is refreshed.

---

## Phase 7: User Story 5 — Delete a Task (Priority: P2)

**Goal**: Users can delete tasks they no longer need with a confirmation step.

**Independent Test**: Sign in → select task → click delete → confirm → verify task removed

### Implementation for User Story 5

- [X] T039 [US5] Create DELETE /api/{user_id}/tasks/{id} endpoint in `backend/routes/tasks.py` — delete task, validate ownership
- [X] T040 [US5] Add delete button with confirmation dialog to TaskItem component
- [X] T041 [US5] Wire delete action to API client DELETE call, remove task from UI without page reload

**Checkpoint**: User can delete tasks. Confirmation prevents accidental deletion.

---

## Phase 8: User Story 6 — Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status with immediate visual feedback.

**Independent Test**: Sign in → click complete toggle on pending task → verify visual change → toggle back

### Implementation for User Story 6

- [X] T042 [US6] Create PATCH /api/{user_id}/tasks/{id}/complete endpoint in `backend/routes/tasks.py` — toggle completed boolean, validate ownership
- [X] T043 [US6] Add completion toggle (checkbox/button) to TaskItem component with visual indicators (strikethrough, checkmark)
- [X] T044 [US6] Wire toggle to API client PATCH call, update UI immediately

**Checkpoint**: User can toggle task completion. Visual feedback is immediate.

---

## Phase 9: User Story 7 — Assign Priority & Tags (Priority: P3)

**Goal**: Users can assign priority levels and tags/categories to tasks for organization.

**Independent Test**: Create task → set priority to "high" → add tags "work", "urgent" → verify displayed

### Implementation for User Story 7

- [X] T045 [US7] Add priority and tags fields to TaskForm component — priority dropdown (high/medium/low), tags input
- [X] T046 [US7] Update POST and PUT endpoints to accept/validate priority and tags fields
- [X] T047 [US7] Display priority badge (color-coded) and tag labels in TaskItem component

**Checkpoint**: Users can assign and view priorities and tags on tasks.

---

## Phase 10: User Story 8 — Search & Filter Tasks (Priority: P3)

**Goal**: Users can search by keyword and filter by status, priority, or tag.

**Independent Test**: Create tasks with different properties → use search bar → apply filters → verify correct results

### Implementation for User Story 8

- [X] T048 [US8] Add query parameters to GET /api/{user_id}/tasks: search, status, priority, tag — implement filtering logic in backend
- [X] T049 [US8] Create SearchFilter component: `frontend/src/components/SearchFilter.tsx` — search bar, status dropdown, priority dropdown, tag selector
- [X] T050 [US8] Wire search/filter controls to API client with query parameters, update task list on change

**Checkpoint**: Users can search and filter tasks. Multiple filters work together (AND logic).

---

## Phase 11: User Story 9 — Sort Tasks (Priority: P3)

**Goal**: Users can sort tasks by created date, priority, or title.

**Independent Test**: Create multiple tasks → change sort order → verify correct reordering

### Implementation for User Story 9

- [X] T051 [US9] Add sort query parameter to GET /api/{user_id}/tasks: sort_by (created_at, priority, title), sort_order (asc, desc) — implement sorting in backend
- [X] T052 [US9] Create SortControls component: `frontend/src/components/SortControls.tsx` — sort dropdown/buttons
- [X] T053 [US9] Wire sort controls to API client with query parameters, update task list on change

**Checkpoint**: Users can sort tasks. Sort applies immediately without page reload.

---

## Phase 12: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements across all user stories

- [X] T054 [P] Backend API tests: `backend/tests/test_tasks.py` — test all 6 endpoints with valid/invalid inputs
- [X] T055 [P] Add proper error handling and user-friendly error messages across frontend
- [X] T056 Responsive design verification — ensure dashboard works on mobile and desktop
- [X] T057 [P] Security hardening — input sanitization, XSS prevention, SQL injection protection
- [X] T058 Run quickstart.md validation — verify setup instructions work end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **US1 Auth (Phase 3)**: Depends on Foundational — BLOCKS US2-US9 (need auth to create tasks)
- **US2 Add Task (Phase 4)**: Depends on US1 Auth
- **US3 View Tasks (Phase 5)**: Depends on US2 Add Task (need tasks to view)
- **US4-US6 (Phases 6-8)**: Depend on US3 View Tasks — can proceed in parallel
- **US7 Priority/Tags (Phase 9)**: Depends on US2 (extends task creation)
- **US8-US9 (Phases 10-11)**: Depend on US7 (filter/sort by priority/tags)
- **Polish (Phase 12)**: Depends on all user stories being complete

### Within Each User Story

- Backend endpoint before frontend component
- API client wiring before UI integration
- Core implementation before polish

### Parallel Opportunities

- T002, T003, T004, T005, T006, T007 can all run in parallel (Phase 1)
- T015, T016 can run in parallel with T011-T014 (Phase 2)
- US4, US5, US6 can run in parallel after US3 is complete
- US8, US9 can run in parallel after US7 is complete
- T054, T055, T057 can run in parallel (Phase 12)

---

## Implementation Strategy

### MVP First (US1 + US2 + US3)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: Auth (US1)
4. Complete Phase 4: Add Task (US2)
5. Complete Phase 5: View Tasks (US3)
6. **STOP and VALIDATE**: Core CRUD MVP working

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add Auth → Users can register/login
3. Add Create + View → Core task management (MVP!)
4. Add Update + Delete + Complete → Full CRUD
5. Add Priority/Tags → Organization
6. Add Search/Filter/Sort → Usability
7. Polish → Production-ready

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story
- Each user story should be independently completable and testable
- Backend endpoints before frontend components
- Stop at any checkpoint to validate story independently
