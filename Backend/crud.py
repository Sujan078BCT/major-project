from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate
from utilis import hash_password

def user_create(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        first_name=user.first_name,
        last_name=user.last_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def check_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()

def check_username(db: Session, user_username: str):
    return db.query(User).filter(User.username == user_username).first()

def user_get(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def user_update(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.first_name:
        db_user.first_name = user.first_name
    if user.last_name:
        db_user.last_name = user.last_name
    db.commit()
    db.refresh(db_user)
    return db_user
