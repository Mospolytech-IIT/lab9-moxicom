"""main.py"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from crud import (create_user, create_post, get_users, get_posts, update_user_email,
                  update_post_content, delete_post, delete_user_and_posts,
                  get_posts_by_user)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    """get session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", tags=["users"])
def create_new_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    """create new user"""
    return create_user(db, username, email, password)

@app.get("/users/", tags=["users"])
def read_users(db: Session = Depends(get_db)):
    """read users"""
    return get_users(db)

@app.put("/users/", tags=["users"])
def update_user(user_id: int, new_email: str, db: Session = Depends(get_db)):
    """update user"""
    return update_user_email(db, user_id, new_email)

@app.delete("/users/", tags=["users"])
def delete_user_with_posts(user_id, db: Session = Depends(get_db)):
    """delete user"""
    return delete_user_and_posts(db, user_id)

#

@app.post("/posts/", tags=["posts"])
def create_new_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    """create new post"""
    return create_post(db, title, content, user_id)

@app.get("/posts/", tags=["posts"])
def read_posts(db: Session = Depends(get_db)):
    """read posts"""
    return get_posts(db)

@app.get("/posts/users/", tags=["posts"])
def read_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    """get posts by user"""
    return get_posts_by_user(db, user_id)

@app.put("/posts/", tags=["posts"])
def update_posts(post_id: int, new_content: str, db: Session = Depends(get_db)):
    """update posts"""
    return update_post_content(db, post_id, new_content)

@app.delete("/posts/", tags=["posts"])
def delete_post_api(post_id: int, db: Session = Depends(get_db)):
    """delete posts"""
    return delete_post(db, post_id)
