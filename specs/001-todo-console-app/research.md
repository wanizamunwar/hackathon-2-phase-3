# Research for In-Memory Python Console Todo App

## Overview
This document summarizes the research and technical decisions for Phase I of the "Evolution of Todo" project, focusing on an in-memory Python console application. Due to the simplicity of the phase and the clear constraints, extensive research was not required.

## Technical Stack Confirmation
**Decision**: Python 3.x (latest stable, e.g., 3.10+)
**Rationale**: Aligns with the project requirements for a Python console application. Python's standard library provides all necessary functionalities without external dependencies for this phase.
**Alternatives considered**: None, as Python is a hard requirement for Phase I.

## Storage Mechanism
**Decision**: In-memory data structures (e.g., list of dictionaries or custom Task objects)
**Rationale**: Explicitly defined constraint for Phase I to simplify development and focus on core logic.
**Alternatives considered**: File-based storage, SQLite (rejected due to "in-memory only" constraint).

## Testing Framework
**Decision**: `pytest`
**Rationale**: `pytest` is a widely adopted, easy-to-use, and powerful testing framework for Python, aligning with the "Test-Driven Development (TDD)" principle.
**Alternatives considered**: `unittest` (rejected due to `pytest`'s superior features and community adoption).
