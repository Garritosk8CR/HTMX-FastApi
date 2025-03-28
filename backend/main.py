from fastapi import FastAPI, Request, Header, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

from uuid import uuid4
from typing import Annotated, Union


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/todos', response_class=HTMLResponse)
async def todos(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):
    if hx_request:
        return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})
    return JSONResponse(content=jsonable_encoder(todos))

@app.put('/todos/{todo_id}', response_class=HTMLResponse)
async def update_todo(todo_id: str, request: Request, text: Annotated[str, Form()]):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todo.txt = text
            break
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})

@app.post('/todos', response_class=HTMLResponse)
async def add_todo(request: Request, todo: Annotated[str, Form()]):  
    if todo:
        todos.append(TODO(todo))
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})


class TODO():
    def __init__(self, txt: str):
        self.id = uuid4()
        self.txt = txt
        self.done = False

todos = [
    {
        "id": "1",
        "txt": "Buy groceries",
        "done": False
    }
]

import uvicorn
uvicorn.run("main:app", host="127.0.0.1", port=8006, reload=True)
