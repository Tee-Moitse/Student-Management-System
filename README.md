# Student Management System

A command-line application for managing student records: adding, searching, viewing, updating, and deleting students, built in Python with a focus on clean, testable design.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tests](https://img.shields.io/badge/tests-unittest-brightgreen)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

## Overview

This project simulates a simple student records system: storing each student's name, age, course, and marks, and supporting the core operations you'd expect from a real management tool. It was built as a hands-on learning project, with particular attention paid to writing code that is easy to test, extend, and maintain, not just code that "works."

## Key Features

- Add students to the database
- Search for a student by name
- View all students in a clean, readable format
- Update a student's course, marks, or other details
- Delete a student's record
- Unit-tested core logic, covering both expected use and edge cases

## Skills Demonstrated

- Writing modular, testable Python functions decoupled from I/O
- Unit testing with Python's built-in unittest framework, including edge-case coverage
- Debugging real logic errors found during test-driven refactoring
- Iterative refactoring of an existing codebase toward better design, function by function
- Clear documentation of design decisions and trade-offs

## Tech Stack

- Language: Python 3
- Testing: unittest (Python standard library)
- Dependencies: none, pure standard library, no external packages required

## Project Structure

```
Student-Management-System/
├── main.py            # Core logic: add, search, view, update, delete
├── database.py        # In-memory student records (student_database)
├── tests/
│   └── test_main.py   # Unit tests for all core functions
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.x installed

### Installation
```bash
git clone https://github.com/<your-username>/Student-Management-System.git
cd Student-Management-System
```

No external dependencies to install, the project runs on the Python standard library alone.

### Running the Program
```bash
python main.py
```

## Usage Examples

Each core function is designed to be called with explicit arguments, making it simple to use programmatically or hook up to a different interface later.

```python
from database import student_database
from main import add_student, search_student, view_students, update_student_info, delete_student

add_student(student_database, {"name": "Kay", "age": 22, "course": "Culinary", "marks": 62.4})

student = search_student(student_database, "Lisa")

print(view_students(student_database))

update_student_info(student_database, "Tom", {"course": "Agriculture", "marks": 70.1})

delete_student(student_database, "Lisa")
```

## Function Reference

| Function | Description | Returns |
|---|---|---|
| add_student(database, student) | Adds a new student record | The added student |
| search_student(database, name) | Finds a student by name | The matching student, or None |
| view_students(database) | Formats all students for display | A multi-line string |
| update_student_info(database, name, update) | Updates a student's fields | The updated student, or None |
| delete_student(database, name) | Removes a student by name | The removed student, or None |

Each student record follows this structure:
```python
{"name": str, "age": int, "course": str, "marks": float}
```

## Design Decisions

The core functions accept the database and any values they need as explicit parameters, rather than reading from global state or calling input() internally. This keeps the logic predictable, the same inputs always produce the same outputs, and makes each function straightforward to unit test in isolation. Any interactive, user-facing input handling is kept separate from this core logic layer.

## Testing

Run the full test suite:
```bash
python -m unittest tests/test_main.py -v
```

Tests cover both standard use cases and edge cases, including:
- Searching for a student who doesn't exist
- Updating or deleting a student not in the database
- Behavior against an empty database

## Roadmap

- [ ] Persistent storage (JSON file or SQLite database)
- [ ] Input validation (valid marks range, positive age)
- [ ] Duplicate-student detection on add
- [ ] Web interface (Flask/Django) reusing the existing core logic

## Author

**Tetlanyo Moitse**
Software Engineer.





