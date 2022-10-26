from turtle import pos
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel): 
    title : str
    content : str
    published : bool = True
    rating: Optional[int] = None


my_posts = [{ "title": "title of post 1", "content": "content of post 1", "id": 1 },
            { "title": "fav foods", "content": "jerk chicken!", "id": 2 } ]

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

@app.get("/")
def root():
    return {"message": "yooooooooo"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000000)
    my_posts.append(post_dict)
    return {'data': my_posts}

@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(int(id))
    return {f'post details: {post}'}