from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session

from app.crud import users as crud
from app.schemas import users as schemas
from app.db.database import get_db

router = APIRouter(
    prefix="/register",
    tags=["register"]
)
@router.post("/", response_model=schemas.User, status_code=201)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    return crud.create_user(db=db, user=user)
