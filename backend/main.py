from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv
from app.db.models import Base

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./research_dashboard.db")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    # For SQLite, we need to enable foreign key support
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="Research Dashboard API",
    description="API for the AI Research Dashboard application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return JSONResponse({
        "message": "Welcome to the Research Dashboard API",
        "status": "active",
        "version": "1.0.0"
    })

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        # Test database connection
        db.execute("SELECT 1")
        db_status = "up"
    except Exception as e:
        db_status = "down"
        print(f"Database connection error: {str(e)}")
    
    return JSONResponse({
        "status": "healthy",
        "services": {
            "api": "up",
            "database": db_status
        }
    }) 