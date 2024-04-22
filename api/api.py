from fastapi import APIRouter, Depends
from api.schemas import PostRequest, PostResponse
from api.repository import QuizRepository
from api.service import QuizService

router = APIRouter(
    prefix='/api',
    tags=['api']
)

# creating dependencies  
quiz_repository = QuizRepository()
quiz_service = QuizService(quiz_repository)

def get_quiz_service() -> QuizService:
    return quiz_service


@router.post('', response_model=PostResponse)
async def create_question(question_num: PostRequest,
                          service: QuizService = Depends(get_quiz_service)) -> PostResponse:
    question_counter = question_num.questions_num
    response = await service.create_question(question_counter)
    return response