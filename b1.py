import os

from fastapi import Body, FastAPI

app = FastAPI()
print("✅ Running File:", os.path.abspath(__file__))

MOVIE = [
    {'category':'science'  , 'title':'Open Heimer'       , 'author':'Author 1'},
    {'category':'Comedy'   , 'title':'Dumb and Dumber'   , 'author':'Author 2'},
    {'category':'Action'   , 'title':'Mission Impossible', 'author':'Author 3'},
    {'category':'Thriller' , 'title':'SAVI'              , 'author':'Author 4'},
    {'category':'Suspense' , 'title':'Haseen Dilruba'    , 'author':'Author 5'},
    {'category':'Suspense' , 'title':'Haseen Dilruba'    , 'author':'Author 6'},
    {'category':'Suspense' , 'title':'Haseen Dilruba'    , 'author':'Author 7'},
    {'category':'Crime'    , 'title':'Gang of Wasseypur' , 'author':'Author 8'},
    {'category':'Violence' , 'title':'Mirzapur'          , 'author':'Author 8'},
    {'category':'fiction'  , 'title':'Blue Beetle'       , 'author':'Author 9'},
    {'category':'Animated' , 'title':'Sonic'             , 'author':'Author 10'},
    {'category':'fiction'  , 'title':'Iron Man'          , 'author':'Author 11'},
    {'category':'Marvel'   , 'title':'Amazing Spiderman' , 'author':'Author 12'},
    {'category':'DC'       , 'title':'Dark Knight'       , 'author':'Author 13'},
]

@app.get("/movies")
async def read_all_movies():
    return MOVIE

@app.get("/movies/my_fav_movie")
async def read_all_movies():
    return {"My favourite movie" : "Iron Man"}
# FastAPI Runs the Endpoints in chronological order so we can not
# use dynamic_param function before it

@app.get("/movies/{movie}")
def read_all_movies(movie: str):
    for mov in MOVIE:
        if mov.get('title').casefold() == movie.casefold():
            return mov
        
@app.get("/movies/")
def get_movie_by_query(category : str):
    movie_to_return = []
    for i in MOVIE:
        if i.get('category').casefold() == category.casefold():
            movie_to_return.append(i)
    return movie_to_return

@app.get("/movies/{movie_author}/")
def read_author_category_by_movie(movie_author: str, category : str):
    movies_to_return = []
    for x in MOVIE:
        if x.get('author').casefold() == movie_author.casefold() and x.get('category').casefold() == category.casefold():
            movies_to_return.append(x)
    return movies_to_return


@app.post("/movies/create_Movie")
async def create_movie(new_movie = Body()):
    MOVIE.append(new_movie)
    return {"POST" : "Done"}


@app.put("/movies/update_movie")
async def update_movie(updated_Movie = Body()):
    for i in range(len(MOVIE)):
        if MOVIE[i].get('title').casefold() == updated_Movie.get('title').casefold():
            MOVIE[i] = updated_Movie
    return {'Update' : 'Done'}

@app.delete("/movies/delete_movie/{delete_movie_title}")
async def delete_movie(delete_movie_title : str):
    for i in range(len(MOVIE)):
        if MOVIE[i].get('title').casefold() == delete_movie_title.casefold():
            MOVIE.pop(i)
            break




