from fastapi import FastAPI
from core.config import CORS_URL
from fastapi.middleware.cors import CORSMiddleware

from db.session import engine
from db.session import Base

from api.endpoints import item
from api.endpoints import user
from api.endpoints import root

# Initialize the database schema
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)
app.include_router(root.router)

# Set up CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    f"http://{CORS_URL}",
    f"http://{CORS_URL}:3000",
    f"http://{CORS_URL}:5173",
    "https://5bqbd24k-5173.aue.devtunnels.ms/",
    "https://5bqbd24k-5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

