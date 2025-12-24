from fastapi import APIRouter, HTTPException, Path, Query, Depends
from sqlalchemy.orm import Session
from typing import List

from app.crud import users as crud

from app.db.database import get_db
from app.core.auth import get_current_active_user

from app.schemas  import users as schemas

router = APIRouter(
    prefix="/users",
    tags = ["users"]
)

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)):
    """Get current user profile"""
    return current_user

# Users endpoints (protected - require authentication)
@router.get("/", response_model=List[schemas.User])
def get_users(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1, le=100), 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Get all users with pagination (requires authentication)"""
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas.User)
def get_user(
    user_id: int = Path(..., gt=0), 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Get a specific user by ID (requires authentication)"""
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int = Path(..., gt=0), 
    user: schemas.UserUpdate = None, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Update an existing user (requires authentication)"""
    db_user = crud.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
def delete_user(
    user_id: int = Path(..., gt=0), 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Delete a user (requires authentication)"""
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {db_user.username} deleted successfully"}
