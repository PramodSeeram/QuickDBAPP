from fastapi import FastAPI, Depends, Request, Form, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models, schemas
from .database import engine, get_db

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="mainapp/templates")
app.mount("/static", StaticFiles(directory="mainapp/static"), name="static")

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return templates.TemplateResponse("index.html", {"request": request, "users": users, "success_message": None})

@app.post("/add_user/")
async def add_user(request: Request, db: Session = Depends(get_db), name: str = Form(...), email: str = Form(...)):
    
    existing_user = db.query(models.User).filter(models.User.email == email).first()
    if existing_user:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "users": db.query(models.User).all(),
            "success_message": "Email already in use!"
        })
    
   
    new_user = models.User(name=name, email=email)
    db.add(new_user)
    db.commit()
    
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "users": db.query(models.User).all(),
        "success_message": "User added successfully!"
    })

@app.get("/update_user/{user_id}")
def update_user_form(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("update_user.html", {"request": request, "user": user})

@app.post("/update_user/{user_id}")
def update_user(request: Request, user_id: int, name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = name
    user.email = email
    db.commit()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "users": db.query(models.User).all(),
        "success_message": "User updated successfully!"
    })

@app.get("/delete_user/{user_id}")
def delete_user(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "users": db.query(models.User).all(),
        "success_message": "User deleted successfully!"
    })
