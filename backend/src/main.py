from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from .api.routes import tasks
from .api.routes import auth
from .core.config import settings
from .core.database import engine
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create all database tables
    print("Creating database tables...")
    try:
        # Create all tables with the new schema
        SQLModel.metadata.create_all(engine)
        print("Database tables created successfully with new schema")
    except Exception as e:
        print(f"Error creating database tables: {e}")
        raise
    yield
    # Shutdown: Cleanup can go here if needed
    print("Application shutdown")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(
        title="Todo App Backend API",
        description="Secure, JWT-authenticated backend API for task management",
        version="1.0.0",
        lifespan=lifespan
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
        # Expose the authorization header to client-side applications
        #expose_headers=["Access-Control-Allow-Origin", "Authorization"]
    )

    # Include API routes
    app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

    @app.get("/")
    def read_root():
        return {"message": "Todo App Backend API", "version": "1.0.0"}

    return app


# Create the application instance
app = create_app()