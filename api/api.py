from fastapi import APIRouter

from schemas import PostRequest


router = APIRouter(
    prefix='/',
    tags=['api']
)


@router.post('')
async def create_question(question_num: PostRequest):
    pass 