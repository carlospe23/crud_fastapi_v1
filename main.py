from datetime import datetime
from uuid import uuid4 as uid
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Text, Optional

app = FastAPI()

class Post(BaseModel):
    id: Optional[str]
    title: str
    autor: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    publish: bool = False


posts = []

@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts')
def save_post(post: Post):
    post.id = str(uid())
    posts.append(post.dict())
    return JSONResponse(content={'message':'saved succesfully'})


@app.get('/posts/{post_id}')
def get_post(post_id:str):
    result = list(filter(lambda post: post['id'] == post_id, posts))
    if not result:
        return JSONResponse(content={'message':'Not found'}, status_code=404)
    return result


@app.delete('/posts/{post_id}')
def delete_post(post_id:str):
    result = list(filter(lambda post: post['id'] == post_id, posts))
    if not result:
        return JSONResponse(content={'message':'Not found'}, status_code=404)
    posts.remove(posts['id']==post_id)
    return JSONResponse(content={'data':'succesfully deleted'}, status_code=200)