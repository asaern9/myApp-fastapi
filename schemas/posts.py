from pydantic import BaseModel


class Post(BaseModel):
    userID: int
    id: int
    title: str
    body: str

