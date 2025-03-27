from fastapi import FastAPI, Request, Header, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

from uuid import uuid4
from typing import Annotated, Union


app = FastAPI()
