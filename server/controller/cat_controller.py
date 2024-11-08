from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.schemas.cat import Cat, CatCreate
from server.repository.cat_repository import get_cats, create_cat
from server.dependencies import get_db

router = APIRouter()

@router.get("/cats/", response_model=list[Cat])
def read_cats(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cats = get_cats(db, skip=skip, limit=limit)
    return cats

@router.post("/cats/", response_model=Cat)
def create_cat(cat: CatCreate, db: Session = Depends(get_db)):
    return create_cat(db=db, cat=cat) 