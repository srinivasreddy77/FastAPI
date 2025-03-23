from pydantic import BaseModel


class Book(BaseModel):
    id:int
    title: str
    author: str
    publisher: str
    language: str
    pagecount: int
    published_date: str
  
class BookUpdateModel(BaseModel):
    title: str
    author: str