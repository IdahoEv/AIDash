from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

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
async def health_check():
    return JSONResponse({
        "status": "healthy",
        "services": {
            "api": "up",
            "database": "up"
        }
    }) 