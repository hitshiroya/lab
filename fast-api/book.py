from fastapi import  FastAPI, Path
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: str
    name: str
    author: str
    rating: str
    published_year: int

    def __init__(self, id, name, author, rating, published_year):
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.published_year = published_year


class Book_Request(BaseModel):
    id: Optional[int] = Field(
        description="id is not required during creation", default=None
    )
    name: str = Field(min_length=3)
    author: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6)
    published_year: int


books = [
    Book(1, "Untold Story", "John Doe", 5, 2025),
    Book(2, "Untold Story1", "John Drake", 5, 2024),
    Book(3, "Untold Story2", "Jim Perry", 2, 2021),
    Book(4, "Untold Story3", "Merc Rons", 4, 2021),
    Book(5, "Untold Story4", "Jack Par", 3, 2019),
]


def generate_book_id(book):
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book


@app.delete("/api/books/{book_id}}")
async def delete_book(delete_id: int = Path(gt=0)):
    for i in range(len(books)):
        if books[i].id == delete_id:
            books.pop(i)
            break


@app.post("/api/create-book")
async def create_books(book_request: Book_Request):
    new_book_store = Book(**book_request.model_dump())
    books.append(generate_book_id(new_book_store))


@app.put("/api/update_book")
async def update_book(updated_book: Book_Request):
    for i in books:
        if i.name == updated_book.name:
            updated_book.author = "Jonty"
    return updated_book


@app.get("/api/books/")
async def get_books_rating(book_rating: int):
    new_book_by_rating = []
    for i in books:
        if i.rating == book_rating:
            new_book_by_rating.append(i)

    return new_book_by_rating


@app.get("/api/books/{book_id}")
async def get_book_by_id(book_id: int = Path(gt=0)):
    for i in range(len(books)):
        if books[i].id == book_id:
            return books[i]


@app.get("/api/books/{publish_year}")
async def get_book_publish_year(publish_year: int):
    new_book_publish_year = []

    for i in books:
        if i.published_year == publish_year:
            new_book_publish_year.append(i)

    return new_book_publish_year


@app.get("/api/books")
async def read_all_books():
    return books
