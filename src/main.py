"""Main application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.routes import router, set_services
from src.application.services import QuestionService, AnswerService
from src.infrastructure.repositories import JsonQuestionRepository, JsonAnswerRepository


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Questionnaire API",
        description="A simple questionnaire API with clean architecture. "
                    "Fill out the questionnaire by getting questions and submitting answers.",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Initialize repositories
    question_repo = JsonQuestionRepository()
    answer_repo = JsonAnswerRepository()
    
    # Initialize services
    question_service = QuestionService(question_repo)
    answer_service = AnswerService(answer_repo)
    
    # Set services for routes
    set_services(question_service, answer_service)
    
    # Include routes
    app.include_router(router, prefix="/api/v1")
    
    @app.get("/", tags=["Health"])
    async def root():
        """Root endpoint."""
        return {
            "message": "Questionnaire API is running",
            "docs": "/docs",
            "version": "0.1.0"
        }
    
    @app.get("/health", tags=["Health"])
    async def health():
        """Health check endpoint."""
        return {"status": "healthy"}
    
    return app


app = create_app()
