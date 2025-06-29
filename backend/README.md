# Research Dashboard Backend

This is the backend service for the Research Dashboard project, built with FastAPI and TensorFlow. The service provides APIs for paper categorization, recommendation, and management.

## Features

- RESTful API endpoints for paper management
- Machine learning-powered paper categorization
- Paper recommendation system
- User authentication and authorization
- Paper metadata extraction and processing
- Search functionality with filters
- PostgreSQL database integration

## Tech Stack

- FastAPI - Modern, fast web framework for building APIs
- TensorFlow - Machine learning framework for paper categorization
- SQLAlchemy - SQL toolkit and ORM
- Alembic - Database migration tool
- PostgreSQL - Production database
- SQLite - Development database
- Pydantic - Data validation and settings management
- PyJWT - JWT token handling for authentication
- pytest - Testing framework
- Poetry - Dependency management and packaging
- psycopg2-binary - PostgreSQL adapter
- asyncpg - Async PostgreSQL driver

## Project Structure

```
backend/
├── app/
│   ├── api/            # API endpoints
│   ├── core/           # Core functionality
│   ├── db/             # Database models and migrations
│   ├── ml/             # Machine learning models
│   ├── schemas/        # Pydantic models
│   └── services/       # Business logic
├── tests/              # Test files
├── alembic/            # Database migrations
├── pyproject.toml      # Poetry project configuration
└── main.py            # Application entry point
```

## Setup

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

3. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```
   # Database Configuration
   DATABASE_URL=postgresql://user:password@localhost:5432/research_dashboard
   DATABASE_TEST_URL=postgresql://user:password@localhost:5432/research_dashboard_test
   
   # For development, you can use SQLite instead:
   # DATABASE_URL=sqlite:///./research_dashboard.db
   
   # Security
   SECRET_KEY=your-secret-key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. Database Setup:
   
   a. Install PostgreSQL (if not already installed):
   - Windows: Download from https://www.postgresql.org/download/windows/
   - macOS: `brew install postgresql`
   - Linux: `sudo apt-get install postgresql`

   b. Create the database:
   ```bash
   # Connect to PostgreSQL
   psql -U postgres
   
   # Create database
   CREATE DATABASE research_dashboard;
   CREATE DATABASE research_dashboard_test;
   ```

   c. Initialize the database:
   ```bash
   poetry run alembic upgrade head
   ```

5. Run the development server:
   ```bash
   poetry run uvicorn main:app --reload
   ```

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Key Endpoints

- `POST /api/v1/papers/` - Add a new paper
- `GET /api/v1/papers/` - List all papers
- `GET /api/v1/papers/{paper_id}` - Get paper details
- `POST /api/v1/papers/categorize` - Categorize a paper
- `GET /api/v1/papers/recommend` - Get paper recommendations
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration

## Development

### Running Tests

```bash
poetry run pytest
```

### Code Style

The project follows PEP 8 guidelines. Use `black` for code formatting:

```bash
poetry run black .
```

### Database Migrations

To create a new migration:
```bash
poetry run alembic revision --autogenerate -m "description"
```

To apply migrations:
```bash
poetry run alembic upgrade head
```

To rollback migrations:
```bash
poetry run alembic downgrade -1  # Roll back one migration
poetry run alembic downgrade base  # Roll back all migrations
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Write or update tests
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
