# AI Research Dashboard

A modern research dashboard for categorizing and recommending scientific papers. Built with FastAPI, ReactJS, and TensorFlow.

## Features
- Paper categorization and organization
- ML-powered paper recommendations
- Interactive dashboard interface
- RESTful API backend

## Tech Stack
- Backend: FastAPI + Python
- Frontend: ReactJS
- ML: TensorFlow
- Database: SQLite (for development)
- Package Management: Poetry

## Setup Instructions

### Backend Setup
1. Install Poetry (if not already installed):
   ```bash
   # Windows (PowerShell)
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   
   # macOS / Linux
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Run the backend server:
   ```bash
   cd backend
   poetry run uvicorn main:app --reload
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Run the development server:
   ```bash
   npm start
   ```

## Project Structure
```
.
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   └── ml/
│   ├── main.py
│   └── pyproject.toml
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   └── services/
    └── package.json
```