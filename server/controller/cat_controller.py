from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from server.schemas.cat import Cat, CatCreate
from server.repository.cat_repository import get_cats, get_cat, create_cat, update_cat, delete_cat
from server.dependencies import get_db

router = APIRouter()

@router.get("/", response_model=list[Cat])
def read_cats(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_cats(db, skip=skip, limit=limit)

@router.get("/{cat_id}", response_model=Cat, responses={404: {"description": "Cat not found"}})
def read_cat(cat_id: int, db: Session = Depends(get_db)):
    db_cat = get_cat(db, cat_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat

@router.post("/", response_model=Cat, status_code=status.HTTP_201_CREATED)
def create_cat_endpoint(cat: CatCreate, db: Session = Depends(get_db)):
    return create_cat(db=db, cat=cat)

@router.put("/{cat_id}", response_model=Cat, responses={404: {"description": "Cat not found"}})
def update_cat_endpoint(cat_id: int, cat: CatCreate, db: Session = Depends(get_db)):
    db_cat = update_cat(db, cat_id, cat)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat

@router.delete("/{cat_id}", response_model=Cat, responses={404: {"description": "Cat not found"}})
def delete_cat_endpoint(cat_id: int, db: Session = Depends(get_db)):
    db_cat = delete_cat(db, cat_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat 