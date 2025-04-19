from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def age_form(request: Request):
    # Initialize age as None for GET requests
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "age": None, "birthdate": None}
    )

@app.post("/", response_class=HTMLResponse)
async def calculate_age(
    request: Request,
    birthdate: str = Form(...)
):
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "age": age, "birthdate": birthdate}
    )