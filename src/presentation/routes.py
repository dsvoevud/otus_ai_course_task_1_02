"""FastAPI routes for the questionnaire API."""
from typing import List
from fastapi import APIRouter, HTTPException, status
from src.domain.models import Question, Answer, AnswerSubmission
from src.application.services import QuestionService, AnswerService

router = APIRouter()

# These will be injected via dependency injection
question_service: QuestionService | None = None
answer_service: AnswerService | None = None


def set_services(q_service: QuestionService, a_service: AnswerService) -> None:
    """Set the services for the router."""
    global question_service, answer_service
    question_service = q_service
    answer_service = a_service


@router.get(
    "/questions",
    response_model=List[Question],
    summary="Get all questions",
    description="Retrieve all available questions from the questionnaire",
    tags=["Questionnaire"]
)
async def get_questions() -> List[Question]:
    """Get all questions from the questionnaire."""
    if question_service is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Service not initialized"
        )
    
    try:
        return question_service.get_questions()
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error loading questions: {str(e)}"
        )


@router.post(
    "/answers",
    status_code=status.HTTP_201_CREATED,
    summary="Submit answers",
    description="Submit answers to the questionnaire. Answers are stored in memory.",
    tags=["Questionnaire"]
)
async def submit_answers(submission: AnswerSubmission) -> dict:
    """Submit answers to the questionnaire."""
    if answer_service is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Service not initialized"
        )
    
    try:
        answer_service.submit_answers(submission.answers)
        return {
            "message": "Answers submitted successfully",
            "count": len(submission.answers)
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error submitting answers: {str(e)}"
        )
