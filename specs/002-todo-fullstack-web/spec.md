# Feature Specification: Todo Full-Stack Web Application

**Feature Branch**: `002-todo-fullstack-web`
**Created**: 2026-02-09
**Status**: Draft
**Input**: User description: "Transform the Phase I console app into a modern multi-user full-stack web application with persistent storage, RESTful API, responsive frontend, and user authentication."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - User Registration & Authentication (Priority: P1)

As a new user, I want to sign up and sign in to the todo application so that my tasks are private and persistent across sessions.

**Why this priority**: Authentication is the foundation for all other features — without it, there is no user isolation, no data ownership, and no multi-user support. Every other feature depends on knowing who the user is.

**Independent Test**: Can be fully tested by navigating to the app, signing up with email/password, logging out, and signing back in. Delivers secure access control.

**Acceptance Scenarios**:

1. **Given** I am a new visitor, **When** I navigate to the signup page and provide a valid email and password, **Then** my account is created and I am redirected to the task dashboard.
2. **Given** I am a registered user, **When** I enter my email and password on the signin page, **Then** I am authenticated and redirected to the task dashboard.
3. **Given** I am a signed-in user, **When** I click the logout button, **Then** my session is ended and I am redirected to the signin page.
4. **Given** I provide an already-registered email during signup, **When** I submit the form, **Then** I see an error message indicating the email is already in use.
5. **Given** I provide incorrect credentials during signin, **When** I submit the form, **Then** I see an error message indicating invalid credentials.
6. **Given** I am not authenticated, **When** I try to access the task dashboard, **Then** I am redirected to the signin page.

---

### User Story 2 - Add a New Task (Priority: P1)

As an authenticated user, I want to create a new task with a title and optional description so that I can track things I need to do.

**Why this priority**: Creating tasks is the most fundamental operation — without it, the app has no purpose. This is the core write operation.

**Independent Test**: Can be tested by signing in, clicking "Add Task", entering a title, and verifying the task appears in the list.

**Acceptance Scenarios**:

1. **Given** I am signed in, **When** I enter a task title (1-200 characters) and submit, **Then** the task is created with status "pending" and appears in my task list.
2. **Given** I am signed in, **When** I enter a title and optional description (max 1000 characters) and submit, **Then** both are saved and visible in task details.
3. **Given** I am signed in, **When** I try to submit a task with an empty title, **Then** I see a validation error and the task is not created.
4. **Given** I am signed in, **When** I create a task, **Then** the task is automatically associated with my user account and is not visible to other users.

---

### User Story 3 - View All Tasks (Priority: P1)

As an authenticated user, I want to view all my tasks in a list so that I can see what I need to do at a glance.

**Why this priority**: Viewing tasks is the core read operation and essential for any task management. Users need to see their tasks to manage them.

**Independent Test**: Can be tested by signing in with a user who has existing tasks and verifying all tasks are displayed with title, status, and created date.

**Acceptance Scenarios**:

1. **Given** I am signed in and have tasks, **When** I navigate to the task dashboard, **Then** I see all my tasks displayed with title, completion status, priority, and created date.
2. **Given** I am signed in and have no tasks, **When** I navigate to the dashboard, **Then** I see an empty state message encouraging me to create my first task.
3. **Given** I am signed in, **When** I view my tasks, **Then** I only see tasks belonging to my account — never tasks from other users.

---

### User Story 4 - Update a Task (Priority: P2)

As an authenticated user, I want to update the title, description, or other details of an existing task so that I can correct mistakes or add information.

**Why this priority**: Editing is essential for practical use but secondary to creating and viewing tasks.

**Independent Test**: Can be tested by signing in, selecting an existing task, modifying its title or description, saving, and verifying the changes persist.

**Acceptance Scenarios**:

1. **Given** I am signed in and viewing a task I own, **When** I edit the title and/or description and save, **Then** the changes are persisted and reflected in the task list.
2. **Given** I am signed in, **When** I try to update a task with an empty title, **Then** I see a validation error and the update is rejected.
3. **Given** I am signed in, **When** I update a task, **Then** the `updated_at` timestamp is refreshed.

---

### User Story 5 - Delete a Task (Priority: P2)

As an authenticated user, I want to delete a task I no longer need so that my task list stays clean and relevant.

**Why this priority**: Deletion is important for list management but secondary to core CRUD operations.

**Independent Test**: Can be tested by signing in, selecting an existing task, confirming deletion, and verifying it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** I am signed in and viewing a task I own, **When** I click delete and confirm, **Then** the task is permanently removed from my list.
2. **Given** I am signed in, **When** I click delete, **Then** I am asked to confirm before the task is actually deleted.
3. **Given** I am signed in, **When** I delete a task, **Then** it is immediately removed from the UI without a full page reload.

---

### User Story 6 - Mark Task as Complete/Incomplete (Priority: P2)

As an authenticated user, I want to toggle a task's completion status so that I can track my progress.

**Why this priority**: Completion tracking is core to a todo app's purpose but depends on tasks existing first.

**Independent Test**: Can be tested by signing in, clicking the complete toggle on a pending task, verifying it shows as completed, and toggling it back.

**Acceptance Scenarios**:

1. **Given** I am signed in and have a pending task, **When** I click the complete toggle, **Then** the task is marked as completed with a visual indicator (strikethrough, checkmark, etc.).
2. **Given** I am signed in and have a completed task, **When** I click the complete toggle, **Then** the task is marked as pending again.
3. **Given** I am signed in, **When** I toggle completion, **Then** the change is persisted and reflected immediately in the UI.

---

### User Story 7 - Assign Priority & Tags (Priority: P3)

As an authenticated user, I want to assign a priority level (high/medium/low) and tags/categories (e.g., work, home, personal) to my tasks so that I can organize them by importance and context.

**Why this priority**: Organization features enhance usability but are not required for the basic task management workflow.

**Independent Test**: Can be tested by creating a task, assigning a priority and tag, and verifying the priority/tag is displayed and persisted.

**Acceptance Scenarios**:

1. **Given** I am creating or editing a task, **When** I select a priority level (high, medium, low), **Then** the priority is saved and displayed with a visual indicator (color/icon).
2. **Given** I am creating or editing a task, **When** I assign one or more tags/categories, **Then** the tags are saved and displayed as labels on the task.
3. **Given** I do not assign a priority, **When** the task is created, **Then** the default priority is "medium".
4. **Given** I do not assign tags, **When** the task is created, **Then** the task has no tags and displays normally.

---

### User Story 8 - Search & Filter Tasks (Priority: P3)

As an authenticated user, I want to search tasks by keyword and filter by status, priority, or tag so that I can quickly find specific tasks.

**Why this priority**: Search and filtering improve usability for users with many tasks but are not essential for basic task management.

**Independent Test**: Can be tested by creating several tasks with different statuses, priorities, and tags, then using the search bar and filter controls to verify correct results.

**Acceptance Scenarios**:

1. **Given** I am signed in and have multiple tasks, **When** I type a keyword in the search bar, **Then** the task list is filtered to show only tasks whose title or description contains that keyword.
2. **Given** I am signed in, **When** I filter by status (all/pending/completed), **Then** only tasks matching the selected status are displayed.
3. **Given** I am signed in, **When** I filter by priority (high/medium/low), **Then** only tasks matching the selected priority are displayed.
4. **Given** I am signed in, **When** I filter by tag/category, **Then** only tasks with the selected tag are displayed.
5. **Given** I apply multiple filters, **When** viewing results, **Then** all filters are applied together (AND logic).

---

### User Story 9 - Sort Tasks (Priority: P3)

As an authenticated user, I want to sort my task list by different criteria so that I can view tasks in the order most useful to me.

**Why this priority**: Sorting enhances usability and task organization but is supplementary to core features.

**Independent Test**: Can be tested by creating multiple tasks with different dates and priorities, then using sort controls to verify correct ordering.

**Acceptance Scenarios**:

1. **Given** I am signed in and have multiple tasks, **When** I sort by created date (newest/oldest first), **Then** tasks are reordered by their creation timestamp.
2. **Given** I am signed in, **When** I sort by priority (high to low or low to high), **Then** tasks are reordered by priority level.
3. **Given** I am signed in, **When** I sort alphabetically by title, **Then** tasks are reordered A-Z or Z-A.
4. **Given** I change the sort order, **When** viewing the list, **Then** the sort preference is applied immediately without a full page reload.

---

### Edge Cases

- What happens when a user tries to access another user's task by manipulating the URL or API call? → 403 Forbidden or 404 Not Found.
- What happens when the JWT token expires mid-session? → User is redirected to signin with a "session expired" message.
- What happens when the database connection is unavailable? → User sees a friendly error message, not a stack trace.
- What happens when a user submits a task title with only whitespace? → Treated as empty, validation error shown.
- What happens when two sessions update the same task simultaneously? → Last write wins, no data corruption.
- What happens when a user searches with special characters? → Characters are escaped, no SQL injection or XSS.
- What happens when there are hundreds of tasks? → Pagination or virtual scrolling prevents performance degradation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to sign up with email and password using Better Auth.
- **FR-002**: System MUST allow users to sign in and receive a JWT token for API authentication.
- **FR-003**: System MUST provide a RESTful API with the following endpoints secured by JWT:
  - `GET /api/{user_id}/tasks` — List all tasks for the user
  - `POST /api/{user_id}/tasks` — Create a new task
  - `GET /api/{user_id}/tasks/{id}` — Get task details
  - `PUT /api/{user_id}/tasks/{id}` — Update a task
  - `DELETE /api/{user_id}/tasks/{id}` — Delete a task
  - `PATCH /api/{user_id}/tasks/{id}/complete` — Toggle completion status
- **FR-004**: System MUST enforce user isolation — each user can only access their own tasks.
- **FR-005**: System MUST validate the JWT token on every API request and return 401 Unauthorized for invalid/missing tokens.
- **FR-006**: System MUST match the user_id in the JWT token with the user_id in the URL path to prevent unauthorized access.
- **FR-007**: System MUST persist all task data in Neon Serverless PostgreSQL via SQLModel ORM.
- **FR-008**: System MUST provide a responsive frontend built with Next.js 16+ (App Router).
- **FR-009**: System MUST support task fields: title (required), description (optional), completed (boolean), priority (high/medium/low), tags (array of strings), created_at, updated_at.
- **FR-010**: System MUST support search by keyword across task title and description.
- **FR-011**: System MUST support filtering tasks by status, priority, and tag.
- **FR-012**: System MUST support sorting tasks by created date, priority, and title.
- **FR-013**: System MUST use the shared BETTER_AUTH_SECRET environment variable for JWT signing and verification across both frontend and backend.

### Key Entities

- **User**: Managed by Better Auth. Key attributes: id (string), email (unique), name, created_at. Users own tasks.
- **Task**: Core entity. Key attributes: id (integer, auto-increment), user_id (foreign key to User), title (string, required), description (text, optional), completed (boolean, default false), priority (enum: high/medium/low, default medium), tags (array of strings, default empty), created_at (timestamp), updated_at (timestamp).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 6 RESTful API endpoints are functional and return correct responses for valid and invalid requests.
- **SC-002**: User signup, signin, and logout work end-to-end with proper session management.
- **SC-003**: A signed-in user can perform full CRUD operations on tasks (create, read, update, delete, toggle complete).
- **SC-004**: User isolation is enforced — no user can see or modify another user's tasks via UI or direct API calls.
- **SC-005**: Tasks persist across sessions — signing out and back in shows previously created tasks.
- **SC-006**: Search, filter, and sort operations work correctly on the frontend with immediate UI updates.
- **SC-007**: The frontend is responsive and usable on desktop and mobile screen sizes.
- **SC-008**: All API endpoints return appropriate HTTP status codes (200, 201, 400, 401, 403, 404, 500).
