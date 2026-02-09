---
id: 001
title: Establish initial constitution for Phase I
stage: constitution
date: 2026-01-03
surface: agent
model: gemini-model
feature: none
branch: unknown
user: unknown
command: /sp.constitution
labels: ["constitution", "phase-1", "hackathon"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:
- none
---

## Prompt

Hello can you help me with thsi hackathon only to develop phase 1 for now and later on we can continue the rest first of all read it and save in your memory: Requirements
You are required to complete the 5-Phase "Evolution of Todo" Project using Claude Code and Spec-Kit Plus. The core deliverables are:
Spec-Driven Implementation: You must implement all 5 Phases of the project (detailed below). You are strictly required to use Spec-Driven Development. You must write a Markdown Constitution and Spec for every feature of the phase, and use Claude Code to generate the implementation.
Constraint: You cannot write the code manually. You must refine the Spec until Claude Code generates the correct output.
Integrated AI Chatbot: In Phases III, IV, and V, you must implement a conversational interface using OpenAI Chatkit, OpenAI Agents SDK, and Official MCP SDK. The bot must be able to manage the user's Todo list via natural language (e.g., "Reschedule my morning meetings to 2 PM").
Cloud Native Deployment: In Phases IV and V, you must deploy the chatbot locally on Minikube, and on the cloud on DigitalOcean Kubernetes (DOKS). 
Todo App Feature Progression
Basic Level (Core Essentials)
These form the foundation—quick to build, essential for any MVP:
Add Task – Create new todo items
Delete Task – Remove tasks from the list
Update Task – Modify existing task details
View Task List – Display all tasks
Mark as Complete – Toggle task completion status
Intermediate Level (Organization & Usability)
Add these to make the app feel polished and practical:


Priorities & Tags/Categories – Assign levels (high/medium/low) or labels (work/home)
Search & Filter – Search by keyword; filter by status, priority, or date
Sort Tasks – Reorder by due date, priority, or alphabetically
Advanced Level (Intelligent Features)
Recurring Tasks – Auto-reschedule repeating tasks (e.g., "weekly meeting")
Due Dates & Time Reminders – Set deadlines with date/time pickers; browser notifications
Use Agentic Dev Stack for building this hackathon project.
Hackathon Phases Overview
Phase
Description
Technology Stack
Points
Due Date
Phase I
In-Memory Python Console App
Python, Claude Code, Spec-Kit Plus
100
Dec 7, 2025
Phase II
Full-Stack Web Application
Next.js, FastAPI, SQLModel, Neon DB
150
Dec 14, 2025
Phase III
AI-Powered Todo Chatbot
OpenAI ChatKit, Agents SDK, Official MCP SDK
200
Dec 21, 2025
Phase IV
Local Kubernetes Deployment
Docker, Minikube, Helm, kubectl-ai, kagent
250
Jan 4, 2026
Phase V
Advanced Cloud Deployment
Kafka, Dapr, DigitalOcean DOKS
300
Jan 18, 2026
TOTAL




1,000




Bonus Points
Participants can earn additional bonus points for exceptional implementations:
Bonus Feature
Points
Reusable Intelligence – Create and use reusable intelligence via Claude Code Subagents and Agent Skills
+200
Create and use Cloud-Native Blueprints via Agent Skills
+200
Multi-language Support – Support Urdu in chatbot
+100
Voice Commands – Add voice input for todo commands
+200
TOTAL BONUS
+600



Timeline
Submission Deadline: On Sundays on dates as mentioned above.
Live Presentations: On Sundays, December 7, 14, and 21, 2025 and on January 4 and 18, 2026 starting at 8:00 PM on Zoom. Final Live Presentation date to be determined.

Top submissions will be invited via WhatsApp to present live on Zoom. 
Note: All submissions will be evaluated. Live presentation is by invitation only, but does not affect final scoring. 
Milestone
Date
Description
Hackathon Start
Monday, Dec 1, 2025
Documentation released
Phase I Due
Sunday, Dec 7, 2025
Console app checkpoint
Phase II Due
Sunday, Dec 14, 2025
Web app checkpoint
Phase III Due
Sunday, Dec 21, 2025
Chatbot checkpoint
Phase IV Due
Sunday, Jan 4, 2026
Local K8s checkpoint
Final Submission
Sunday, Jan 18, 2026
All phases complete
Live Presentations
Sundays, Dec 7, 14, 21, and Jan 4 and 18
Top submissions present
/sp.constitution run this for phase 1 now and first we will go with this. like all other commands latter.

## Response snapshot

The project constitution has been updated to Version 1.0.0, establishing core principles and governance for Phase I of the "Evolution of Todo" project.

## Outcome

- ✅ Impact: Successfully established the initial project constitution, defining core principles, development constraints, quality gates, and governance for Phase I of the hackathon project.
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Proceed with creating the spec for Phase I.
- 🧠 Reflection: The constitution was successfully updated, ensuring alignment with Spec-Driven Development. The process highlighted the need for a more robust PHR creation mechanism that is platform-independent.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script failed to execute on Windows due to it being a bash script, requiring manual PHR creation.
- Graders run and results (PASS/FAIL): N/A (manual PHR creation)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Develop a platform-agnostic PHR creation tool or a PowerShell equivalent for `create-phr.sh`.
