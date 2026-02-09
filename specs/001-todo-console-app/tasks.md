# Tasks: In-Memory Python Console Todo App

**Input**: Design documents from `specs/001-todo-console-app/`
**Prerequisites**: `plan.md`, `spec.md`, `data-model.md`, `research.md`, `quickstart.md`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directories: `src/todo_app/` and `tests/unit/`
- [X] T002 Create main application entry point: `src/__main__.py`
- [X] T003 [P] Initialize `__init__.py` files in `src/` and `src/todo_app/`
- [X] T004 Create `requirements.txt` with `pytest`
- [X] T005 [P] Configure a basic `.gitignore` (e.g., for `__pycache__`, `.pytest_cache`, `venv/`)

---

## Phase 2: Foundational (Core Task Management)

**Purpose**: Establish core `Task` entity and `TaskManager` (blocking prerequisites)

- [X] T006 Create `src/todo_app/models.py` for `Task` entity definition
- [X] T007 Create `src/todo_app/manager.py` for `TaskManager` class (initial structure)
- [X] T008 [P] Create `tests/unit/test_models.py` for `Task` entity unit tests

---

## Phase 3: User Story 1 - Add a New Todo Task (Priority: P1)

**Goal**: Enable adding new tasks with descriptions, and validate input.

**Independent Test**: Add a task and verify its presence using view functionality.

### Tests for User Story 1

- [X] T009 [P] [US1] Create `tests/unit/test_manager.py` (initial setup)
- [X] T010 [US1] Write test for `TaskManager.add_task` in `tests/unit/test_manager.py` (ensure task creation, ID generation)
- [X] T011 [US1] Write test for `TaskManager.add_task` with empty description in `tests/unit/test_manager.py` (expect error)

### Implementation for User Story 1

- [X] T012 [US1] Implement `TaskManager.add_task` in `src/todo_app/manager.py` (generate unique ID, store task)
- [X] T013 [US1] Add input validation for `add_task` description (not empty) in `src/todo_app/manager.py`

---

## Phase 4: User Story 2 - View All Todo Tasks (Priority: P1)

**Goal**: Display all tasks with ID, description, and status.

**Independent Test**: Add tasks, then display to verify all are shown correctly.

### Tests for User Story 2

- [X] T014 [US2] Write test for `TaskManager.get_all_tasks` with multiple tasks in `tests/unit/test_manager.py`
- [X] T015 [US2] Write test for `TaskManager.get_all_tasks` with no tasks in `tests/unit/test_manager.py` (expect empty list)

### Implementation for User Story 2

- [X] T016 [US2] Implement `TaskManager.get_all_tasks` in `src/todo_app/manager.py` (return list of Task objects)
- [X] T017 [US2] Implement console output formatting for tasks in `src/todo_app/cli.py` (later main.py integration)

---

## Phase 5: User Story 3 - Mark a Task as Complete (Priority: P1)

**Goal**: Change a task's status to complete using its ID.

**Independent Test**: Mark a task complete, then view to confirm status change.

### Tests for User Story 3

- [X] T018 [US3] Write test for `TaskManager.mark_task_complete` for existing task in `tests/unit/test_manager.py`
- [X] T019 [US3] Write test for `TaskManager.mark_task_complete` with non-existent ID in `tests/unit/test_manager.py` (expect error)
- [X] T020 [US3] Write test for `TaskManager.mark_task_complete` on already complete task in `tests/unit/test_manager.py`

### Implementation for User Story 3

- [X] T021 [US3] Implement `TaskManager.mark_task_complete` in `src/todo_app/manager.py`
- [X] T022 [US3] Add validation for task ID existence in `TaskManager.mark_task_complete` in `src/todo_app/manager.py`

---

## Phase 6: User Story 4 - Update an Existing Todo Task (Priority: P2)

**Goal**: Modify a task's description using its ID.

**Independent Test**: Update a task's description, then view to confirm change.

### Tests for User Story 4

- [X] T023 [US4] Write test for `TaskManager.update_task_description` for existing task in `tests/unit/test_manager.py`
- [X] T024 [US4] Write test for `TaskManager.update_task_description` with non-existent ID in `tests/unit/test_manager.py` (expect error)
- [X] T025 [US4] Write test for `TaskManager.update_task_description` with empty new description in `tests/unit/test_manager.py` (expect error)

### Implementation for User Story 4

- [X] T026 [US4] Implement `TaskManager.update_task_description` in `src/todo_app/manager.py`
- [X] T027 [US4] Add validation for task ID existence and non-empty description in `TaskManager.update_task_description` in `src/todo_app/manager.py`

---

## Phase 7: User Story 5 - Delete a Todo Task (Priority: P2)

**Goal**: Remove a task from the list using its ID.

**Independent Test**: Delete a task, then view to confirm its removal.

### Tests for User Story 5

- [X] T028 [US5] Write test for `TaskManager.delete_task` for existing task in `tests/unit/test_manager.py`
- [X] T029 [US5] Write test for `TaskManager.delete_task` with non-existent ID in `tests/unit/test_manager.py` (expect error)

### Implementation for User Story 5

- [X] T030 [US5] Implement `TaskManager.delete_task` in `src/todo_app/manager.py`
- [X] T031 [US5] Add validation for task ID existence in `TaskManager.delete_task` in `src/todo_app/manager.py`

---

## Phase 8: Polish & Cross-Cutting Concerns (CLI Integration, Error Handling)

**Purpose**: Integrate `TaskManager` with the console interface, refine user experience.

- [X] T032 Implement main CLI loop in `src/__main__.py`
- [X] T033 Implement command parsing (add, list, complete, update, delete, quit) in `src/__main__.py`
- [X] T034 Integrate `TaskManager` operations into CLI commands in `src/__main__.py`
- [X] T035 [P] Implement robust error handling for user input (e.g., `ValueError` for non-integer IDs) in `src/__main__.py`
- [X] T036 [P] Implement clear, user-friendly messages for all operations and errors in `src/__main__.py`
- [X] T037 [P] Update `quickstart.md` with final command examples.
- [X] T038 Review all unit tests in `tests/unit/` for completeness and coverage.
- [X] T039 Run all unit tests to ensure all features work as expected.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational phase completion. Can proceed in parallel if different aspects (tests vs impl) or different user stories are assigned to different developers.
- **Polish (Final Phase 8)**: Depends on all user stories being functionally complete.

### User Story Dependencies

- All user stories (US1-US5) primarily depend on the foundational `Task` entity and `TaskManager`. Once Foundational (Phase 2) is complete, user stories can conceptually be implemented in parallel, but will be prioritized by P1 then P2.

### Within Each User Story

- Tests MUST be written and FAIL before implementation (`T009-T011` before `T012-T013`, etc.)
- Models (e.g., `Task`) before managers (`TaskManager`).
- Core manager logic before CLI integration.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel.
- `T008` (Task entity tests) can be done in parallel with `T006` and `T007` (Task entity and manager initial structure).
- Within user story phases, test tasks marked [P] can run in parallel with each other.
- The polish phase (Phase 8) has parallel tasks for error handling and messages.

---

## Implementation Strategy

### MVP First (User Story 1, 2, 3)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1 (Add)
4.  Complete Phase 4: User Story 2 (View)
5.  Complete Phase 5: User Story 3 (Mark Complete)
6.  **STOP and VALIDATE**: Test User Stories 1, 2, and 3 independently.
7.  Proceed to Phase 8 (initial CLI integration for MVP) for early demo/feedback.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 (Add) → Test independently.
3.  Add User Story 2 (View) → Test independently.
4.  Add User Story 3 (Mark Complete) → Test independently.
5.  Add User Story 4 (Update) → Test independently.
6.  Add User Story 5 (Delete) → Test independently.
7.  Integrate with CLI in Phase 8.

### Parallel Team Strategy
*(Not applicable for a single-agent implementation.)*

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group (when Git commands are enabled)
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
