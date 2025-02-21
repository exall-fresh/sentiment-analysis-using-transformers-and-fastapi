from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .sentiment_analysis import sentiment_pipeline

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .app import *  # Import routes
