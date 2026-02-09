# Quickstart: In-Memory Python Console Todo App

This document provides instructions on how to set up and run the Phase I "Evolution of Todo" console application.

## Prerequisites
*   Python 3.x installed on your system.

## Setup
1.  **Clone the repository** (if not already done):
    ```bash
    # Assuming you are in the parent directory of 'Phase 1'
    # git clone <repository_url> Phase 1
    # cd Phase 1
    ```
2.  **Navigate to the project root**:
    ```bash
    cd <path_to_your_project_root> # e.g., C:\Vanilla_session\Phase 1
    ```

## Running the Application
The application can be run directly from the command line.

```bash
python -m src.todo_app
```

## Basic Usage
Once the application is running, you will be presented with a menu of options. Enter the corresponding number or 'q' to interact with the Todo list.

Menu options:
*   `1`: Add a new task.
*   `2`: View all tasks.
*   `3`: Mark a task as complete.
*   `4`: Update a task's description.
*   `5`: Delete a task.
*   `q`: Quit the application.

## Testing
To run the unit tests for the application:

1.  Ensure `pytest` is installed:
    ```bash
    pip install pytest
    ```
2.  Run tests from the project root:
    ```bash
    pytest tests/unit
    ```
