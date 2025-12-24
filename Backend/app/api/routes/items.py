from fastapi import  HTTPException, Path, Query, Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.crud import items as  crud
from app.db.database import  get_db
from app.schemas  import items as schemas,users as user_schema
from app.core.auth import get_current_active_user

router = APIRouter(
    prefix="/items",
    tags=["items"]
)
# Items endpoints (public)
@router.get("/", response_model=List[schemas.Item],tags=["items"])
def get_items(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db)):
    """Get all items with pagination"""
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=schemas.Item,tags=["items"])
def get_item(item_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    """Get a specific item by ID"""
    item = crud.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Items endpoints (protected - require authentication)
@router.post("/", response_model=schemas.Item, status_code=201,tags=["items"])
def create_item(
    item: schemas.ItemCreate, 
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_active_user)
):
    """Create a new item (requires authentication)"""
    return crud.create_item(db=db, item=item)

@router.put("/{item_id}", response_model=schemas.Item,tags=["items"])
def update_item(
    item_id: int = Path(..., gt=0), 
    item: schemas.ItemUpdate = None, 
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_active_user)
):
    """Update an existing item (requires authentication)"""
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}",tags=["items"])
def delete_item(
    item_id: int = Path(..., gt=0), 
    db: Session = Depends(get_db),
    current_user: user_schema.User = Depends(get_current_active_user)
):
    """Delete an item (requires authentication)"""
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item {db_item.name} deleted successfully"}