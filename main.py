from fastapi import FastAPI
from src.books.routes import book_router
app=FastAPI()

#we have to include the router in the app instance

app.include_router(book_router, prefix="/books", tags=["books"])
