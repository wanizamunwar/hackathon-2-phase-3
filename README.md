# Evolution of Todo - Hackathon Project

## Overview
A 5-Phase "Evolution of Todo" Project using Claude Code and Spec-Kit Plus.

## Core Deliverables
1. **Spec-Driven Implementation**: Implement all 5 Phases using Spec-Driven Development. Write a Markdown Constitution and Spec for every feature, and use Claude Code to generate the implementation.
   - **Constraint**: Cannot write code manually. Must refine the Spec until Claude Code generates the correct output.
2. **Integrated AI Chatbot** (Phases III, IV, V): Conversational interface using OpenAI Chatkit, OpenAI Agents SDK, and Official MCP SDK. Bot must manage Todo list via natural language (e.g., "Reschedule my morning meetings to 2 PM").
3. **Cloud Native Deployment** (Phases IV, V): Deploy chatbot locally on Minikube, and on cloud on DigitalOcean Kubernetes (DOKS).

---

## Todo App Feature Progression

### Basic Level (Core Essentials)
- **Add Task** - Create new todo items
- **Delete Task** - Remove tasks from the list
- **Update Task** - Modify existing task details
- **View Task List** - Display all tasks
- **Mark as Complete** - Toggle task completion status

### Intermediate Level (Organization & Usability)
- **Priorities & Tags/Categories** - Assign levels (high/medium/low) or labels (work/home)
- **Search & Filter** - Search by keyword; filter by status, priority, or date
- **Sort Tasks** - Reorder by due date, priority, or alphabetically

### Advanced Level (Intelligent Features)
- **Recurring Tasks** - Auto-reschedule repeating tasks (e.g., "weekly meeting")
- **Due Dates & Time Reminders** - Set deadlines with date/time pickers; browser notifications

---

## Hackathon Phases

| Phase | Description | Technology Stack | Points | Due Date |
|-------|-------------|-----------------|--------|----------|
| **Phase I** | In-Memory Python Console App | Python, Claude Code, Spec-Kit Plus | 100 | Dec 7, 2025 |
| **Phase II** | Full-Stack Web Application | Next.js, FastAPI, SQLModel, Neon DB | 150 | Dec 14, 2025 |
| **Phase III** | AI-Powered Todo Chatbot | OpenAI ChatKit, Agents SDK, Official MCP SDK | 200 | Dec 21, 2025 |
| **Phase IV** | Local Kubernetes Deployment | Docker, Minikube, Helm, kubectl-ai, kagent | 250 | Jan 4, 2026 |
| **Phase V** | Advanced Cloud Deployment | Kafka, Dapr, DigitalOcean DOKS | 300 | Jan 18, 2026 |
| **TOTAL** | | | **1,000** | |

---

## Bonus Points

| Bonus Feature | Points |
|---------------|--------|
| Reusable Intelligence - Claude Code Subagents and Agent Skills | +200 |
| Cloud-Native Blueprints via Agent Skills | +200 |
| Multi-language Support - Support Urdu in chatbot | +100 |
| Voice Commands - Add voice input for todo commands | +200 |
| **TOTAL BONUS** | **+600** |
