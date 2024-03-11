# Todo List Application

This is a simple todo list application created using Test Driven Development (TDD) methodology.

## Installation

1. Clone the repository:


2. Navigate to the project directory:



3. Install the required dependencies (optional):



## Usage

The application provides a simple interface for managing tasks in a todo list.

1. To add a new task, use the `add_task` method:
```python
from todo_list import TodoList

todo_list = TodoList()
todo_list.add_task("Task 1")


To mark a task as completed, use the mark_task_as_completed method:

python

todo_list.mark_task_as_completed("Task 1")

To delete a task from the list, use the delete_task method:

python
Copy code
todo_list.delete_task("Task 1")

To run the tests, execute the following command:

Copy code
python -m unittest test_todo_list.py
