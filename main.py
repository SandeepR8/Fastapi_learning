from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from schema import PostCreate, PostResponse


app = FastAPI()

templates = Jinja2Templates(directory = "templates")

posts : list[dict] = [
    {
        'id' : 1,
        'author' : 'Corey schafer',
        'content' : 'this is the fastapi framework from Cs',
        'title' : 'Started learning',
        'date':  'April 2025'
    },
    {
        'id' : 2,
        'author' : 'R sandeep',
        'content' : 'Im learning this framework from CS',
        'title' : 'Use of Get',
        'date':  'April 2026'
    }
]

@app.get('/api/posts/' , name='home', response_model = PostResponse)
def get_posts(request : Request):
    return templates.TemplateResponse(request, 'home.html',{'posts' : posts, 'title' : 'home'})

@app.get('/api/posts/{post_id}')
def get_post(post_id : int):
    for post in posts:
        if post.get('id') == post_id :
            return post
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "post not found") 

@app.post(
    '/api/posts',
    response_model = PostResponse,
    status_code = status.HTTP_201_CREATED
)
def Create_post(post : PostCreate):
    new_id = max(p['id'] for p in posts) + 1 if posts else 1
    new_post = {
        'id' : new_id,
        'title' : post.title,
        'content' : post.content,
        'author' : post.author,
        'date' : "June 2026"
    }
    posts.append(new_post)

    return new_post