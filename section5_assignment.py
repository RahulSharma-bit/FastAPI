from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title" : "title 1", "catergory" : "category 1", "author" : "author 1"},
    {"title" : "title 2", "catergory" : "category 2", "author" : "Chaman"},
    {"title" : "title 3", "catergory" : "category 3", "author" : "author 3"},
    {"title" : "title 4", "catergory" : "category 4", "author" : "Chaman"},
    {"title" : "title 5", "catergory" : "category 5", "author" : "author 5"},
]

@app.get("/books/{author}")
async def read_by_author(author : str):
    book_to_return = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author.casefold():
            book_to_return.append(BOOKS[i])
    return book_to_return

# test