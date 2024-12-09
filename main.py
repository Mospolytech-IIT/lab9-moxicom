from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import delete
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Post
from crud import create_user, create_post, get_users, get_posts, update_user_email, update_post_content, delete_post, \
    delete_user_and_posts

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", tags=["users"])
def create_new_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)

@app.get("/users/", tags=["users"])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.put("/users/", tags=["users"])
def update_user(user_id: int, new_email: str, db: Session = Depends(get_db)):
    return update_user_email(db, user_id, new_email)

@app.delete("/users/", tags=["users"])
def delete_user_with_posts(user_id, db: Session = Depends(get_db)):
    return delete_user_and_posts(db, user_id)

#

@app.post("/posts/", tags=["posts"])
def create_new_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    return create_post(db, title, content, user_id)

@app.get("/posts/", tags=["posts"])
def read_posts(db: Session = Depends(get_db)):
    return get_posts(db)

@app.put("/posts/", tags=["posts"])
def update_posts(post_id: int, new_content: str, db: Session = Depends(get_db)):
    return update_post_content(db, post_id, new_content)

@app.delete("/posts/", tags=["posts"])
def delete_post_api(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)

