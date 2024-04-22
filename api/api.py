from fastapi import APIRouter, Depends
from schemas import PostRequest, PostResponse
from repository import QuizRepository
from service import QuizService

router = APIRouter(
    prefix='/api',
    tags=['api']
)

# creating dependencies  
quiz_repository = QuizRepository()
quiz_service = QuizService(quiz_repository)

def get_quiz_service() -> QuizService:
    return quiz_service


@router.post('', )
async def create_question(question_num: PostRequest,
                          service: QuizService = Depends(get_quiz_service)):
    question_counter = question_num.questions_num
    response = await service.create_question(question_counter)
    return response