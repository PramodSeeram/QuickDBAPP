from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models, schemas
from .database import engine, get_db

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# FastAPI app setup
app = FastAPI()

# Template and Static file setup
templates = Jinja2Templates(directory="mainapp/templates")
app.mount("/static", StaticFiles(directory="mainapp/static"), name="static")

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    users = db.query(models.User).all()  # Get all users from DB
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@app.post("/add_user/")
def add_user(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    new_user = models.User(name=name, email=email)
    db.add(new_user)
    db.commit()
    return {"message": "User added successfully!"}

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
