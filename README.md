# Task Management API

A production-ready CRUD API built with FastAPI, PostgreSQL, SQLAlchemy, and Poetry.

## Project Overview

This API allows users to manage tasks with the following features:
- Create, Read, Update, and Delete (CRUD) tasks.
- Task validation using Pydantic.
- Database persistence using PostgreSQL and SQLAlchemy.
- Configuration via environment variables.

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Dependency Management:** Poetry

## Setup Instructions

### Prerequisites

- Python 3.9+
- Poetry
- PostgreSQL Database

### Installation

1.  **Clone the repository** (if applicable).
2.  **Install dependencies:**
    ```bash
    poetry install
    ```
3.  **Environment Setup:**
    - The `.env` file is already created with default values.
    - Update `.env` with your PostgreSQL credentials if they differ from the defaults:
      ```
      DB_HOST=localhost
      DB_PORT=5432
      DB_NAME=task_db
      DB_USER=postgres
      DB_PASSWORD=secret
      ```
    - **Note:** Ensure the database `task_db` exists in your PostgreSQL instance.

### Running the Application


### Running with Docker (Recommended)

1.  **Run with docker-compose:**
    ```bash
    docker-compose -f docker/docker-compose.yml up --build
    ```
    (Or `cd docker && docker-compose up --build`)

2.  **Access the API:**
    - The API will be available at [http://localhost:8000](http://localhost:8000).
    - Database data persists in a docker volume.

3.  **To stop:**
    Press `Ctrl+C` or run `docker-compose down`.

### Running Locally
1.  **Activate the virtual environment:**
    ```bash
    poetry shell
    ```
2.  **Start the server:**
    ```bash
    uvicorn app.main:app --reload
    ```


## API Documentation

Once the server is running, access the interactive API documentation (Swagger UI) at:

http://localhost:8000/docs

## API Endpoints

- **POST /tasks/**: Create a new task.
- **GET /tasks/**: List all tasks.
- **GET /tasks/{id}**: Get a specific task.
- **PUT /tasks/{id}**: Update a task.
- **DELETE /tasks/{id}**: Delete a task.
