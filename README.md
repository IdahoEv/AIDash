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

## Setup Instructions

### Backend Setup
1. Create a virtual environment:
```bash
# python -m venv venv
# source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
poetry install
```

3. Run the backend server:
```bash
cd backend
uvicorn main:app --reload
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
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   └── services/
    └── package.json
```