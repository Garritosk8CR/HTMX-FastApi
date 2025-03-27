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
async def todos(request: Request):
    return JSONResponse(content=jsonable_encoder(todos))


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
