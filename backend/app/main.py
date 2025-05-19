from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import papers

app = FastAPI(
    title="Research Dashboard API",
    description="API for managing and recommending research papers",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(papers.router, prefix="/api/v1", tags=["papers"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Research Dashboard API",
        "docs_url": "/docs",
        "version": "1.0.0"
    } 