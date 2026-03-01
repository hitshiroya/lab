from fastapi import Body, FastAPI

app = FastAPI()


class Book:
    id : str
    name: str
    author: str
    rating: str


    def __init__(self,id,name,author,rating):
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating

books = [
    Book(1,"Untold Story", "John Doe" , 5),
    Book(2,"Untold Story1", "John Drake" , 5),
    Book(3,"Untold Story2", "Jim Perry" , 2),
    Book(4,"Untold Story3", "Merc Rons" , 4),
    Book(5,"Untold Story4", "Jack Par" , 3),
]


@app.delete("/api/delete-book/{delete_title}")
async def delete_book(delete_title: str):
    print(delete_title)
    for i in range(len(books)):
        if books[i].get("name") == delete_title:
            books.pop(i)
            break


@app.post("/api/create-book")
async def create_books(new_book=Body()):
    return books.append(new_book)


@app.put("/api/update_book")
async def update_book(updated_book=Body()):
    for i in books:
        if i.get("name") == updated_book.get("name"):
            i["author"] = "Jims perry"


@app.get("/api/books/{books_by_author}")
async def get_books_by_author(books_by_author: str):
    book_author = []
    for i in range(len(books)):
        if books[i].get("author") == books_by_author:
            book_author.append(books[i])
    return book_author


@app.get("/api/books/{book_identity}")
async def get_specific_book(book_identity):
    for i in books:
        if i["author"] == book_identity:
            return {"data": i}


@app.get("/api/books/{author}")
async def get_books_by_author_and_status(author: str, pubslished: str):
    ans = []
    for i in books:
        if i.get(author) == author and i.get(pubslished) == pubslished:
            ans.append(i)

    return ans


@app.get("/api/books")
async def read_all_books():
    return books
