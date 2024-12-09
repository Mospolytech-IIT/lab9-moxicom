from sqlalchemy.orm import Session
from models import User, Post

def create_user(db: Session, username: str, email: str, password: str):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_post(db: Session, title: str, content: str, user_id: int):
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_users(db: Session):
    return db.query(User).all()

def get_posts(db: Session):
    return db.query(Post).all()

def get_posts_with_users(db: Session):
    return db.query(Post).join(User).all()

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(User).filter(User.id == user_id).first()
    user.email = new_email
    db.commit()
    db.refresh(user)
    return user

def update_post_content(db: Session, post_id: int, new_content: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    post.content = new_content
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(post)
    db.commit()

def delete_user_and_posts(db: Session, user_id: int):
    db.query(Post).filter(Post.user_id == user_id).delete()
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()

