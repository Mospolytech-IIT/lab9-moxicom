"""crud.py"""

from sqlalchemy.orm import Session
from models import User, Post

def create_user(db: Session, username: str, email: str, password: str):
    """create user"""
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_post(db: Session, title: str, content: str, user_id: int):
    """create post"""
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_users(db: Session):
    """get users"""
    return db.query(User).all()

def get_posts(db: Session):
    """get posts"""
    return db.query(Post).all()

def get_posts_with_users(db: Session):
    """get posts with users"""
    return db.query(Post).join(User).all()

def get_posts_by_user(db: Session, user_id: int):
    """get posts by user"""
    return db.query(Post).filter(Post.user_id == user_id).all()

def update_user_email(db: Session, user_id: int, new_email: str):
    """update user email"""
    user = db.query(User).filter(User.id == user_id).first()
    user.email = new_email
    db.commit()
    db.refresh(user)
    return user

def update_post_content(db: Session, post_id: int, new_content: str):
    """update post content"""
    post = db.query(Post).filter(Post.id == post_id).first()
    post.content = new_content
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    """delete post"""
    post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(post)
    db.commit()

def delete_user_and_posts(db: Session, user_id: int):
    """delete user and posts"""
    db.query(Post).filter(Post.user_id == user_id).delete()
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
