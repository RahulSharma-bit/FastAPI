from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Not Required when creating a book", default=None)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new Book",
                "author": "Rahul Sharma",
                "description": "A new description",
                "rating": 5,
                "published_date": 2001
            }
        }
    }


BOOKS = [
    Book(1, "naman Habit", "Falana", "book on self improvement", 5, 2010),
    Book(2, "aman Habit", "Falana", "book on self improvement", 4, 2020),
    Book(3, "Atomic Habit", "Falana", "book on self improvement", 3, 2025),
    Book(4, "chaman Habit", "Falana", "book on self improvement", 4, 2010),
    Book(5, "tappu Habit", "Falana", "book on self improvement", 4, 2007),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item Not Found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    book_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            book_to_return.append(book)
    return book_to_return


@app.get("/book/publish", status_code=status.HTTP_200_OK)
async def read_book_by_date(pub_date: int = Query(gt=1999, lt=2025)):
    list_to_return = []
    for i in range(len(BOOKS)):
        if BOOKS[i].published_date == pub_date:
            list_to_return.append(BOOKS[i])
    return list_to_return


@app.post("/create_a_book", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_request: BookRequest):
    # print(type(book_request))
    # =========================
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(get_book_id(new_book))


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)  # not returning anything.
async def update_a_book(book: BookRequest):
    is_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            is_changed = True
    if not is_changed:
        raise HTTPException(status_code=404, detail="Item Not Found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    is_delete = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            is_delete = True
            break
    if not is_delete:
        raise HTTPException(status_code=404, detail="Item Not Found")


def get_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book
# till now
