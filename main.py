from fastapi import FastAPI, status
from typing import List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
app=FastAPI()

books=[
  {
    "id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publisher": "J.B. Lippincott & Co.",
    "pagecount": 281,
    "language": "English",
    "published_date": "1960-07-11"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "publisher": "Secker & Warburg",
    "pagecount": 328,
    "language": "English",
    "published_date": "1949-06-08"
  },
  {
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Charles Scribner's Sons",
    "pagecount": 180,
    "language": "English",
    "published_date": "1925-04-10"
  },
  {
    "id": 4,
    "title": "Moby-Dick",
    "author": "Herman Melville",
    "publisher": "Harper & Brothers",
    "pagecount": 585,
    "language": "English",
    "published_date": "1851-10-18"
  },
  {
    "id": 5,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "publisher": "T. Egerton, Whitehall",
    "pagecount": 279,
    "language": "English",
    "published_date": "1813-01-28"
  },
  {
    "id": 6,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "publisher": "Little, Brown and Company",
    "pagecount": 277,
    "language": "English",
    "published_date": "1951-07-16"
  },
  {
    "id": 7,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "publisher": "George Allen & Unwin",
    "pagecount": 310,
    "language": "English",
    "published_date": "1937-09-21"
  },
  {
    "id": 8,
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "publisher": "Chatto & Windus",
    "pagecount": 311,
    "language": "English",
    "published_date": "1932-08-31"
  },
  {
    "id": 9,
    "title": "War and Peace",
    "author": "Leo Tolstoy",
    "publisher": "The Russian Messenger",
    "pagecount": 1225,
    "language": "Russian",
    "published_date": "1869-03-01"
  },
  {
    "id": 10,
    "title": "Anna Karenina",
    "author": "Leo Tolstoy",
    "publisher": "The Russian Messenger",
    "pagecount": 864,
    "language": "Russian",
    "published_date": "1877-01-01"
  }
]

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


@app.get("/books",response_model=List[Book])
async def get_all_books():
  return books

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
   new_book=book_data.model_dump()
   books.append(new_book)
   return new_book

@app.get("/book/{book_id}")
async def get_book(book_id:int):
  for book in books:
     if book["id"]==book_id:
        return book
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail="Book is not found in data base")

@app.patch("/books/{book_id}")
async def get_all_books(book_id:int,book_update_data:BookUpdateModel):
  for book in books:
     if book["id"]==book_id:
        book["title"]=book_update_data.title
        book["author"]=book_update_data.author

        return book
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bad request")
  

@app.delete("/book/{book_id}",status_code=status.HTTP_200_OK)
async def delete_book(book_id:int):
   for book in books:
     if book["id"]==book_id:
        books.remove(book)
        return {
           "message":"deleted data successfully"
        }
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No data found with id")