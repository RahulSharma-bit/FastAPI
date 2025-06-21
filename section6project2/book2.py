from fastapi import FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Atomic Habit", "Falana", "book on self improvement", 5),
    Book(2, "Atomic Habit", "Falana", "book on self improvement", 2),
    Book(3, "Atomic Habit", "Falana", "book on self improvement", 3),
    Book(4, "Atomic Habit", "Falana", "book on self improvement", 4),
    Book(5, "Atomic Habit", "Falana", "book on self improvement", 1),
]


@app.get("/books")
async def read_all_books():
    return BOOKS
