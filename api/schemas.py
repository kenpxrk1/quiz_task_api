from pydantic import BaseModel

class PostRequest(BaseModel):
    questions_num: int


class PostResponse(BaseModel):
    question_body: str | None


