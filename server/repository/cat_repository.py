from sqlalchemy.orm import Session
from server.database.models.cat import Cat
from server.schemas.cat import CatCreate

def get_cats(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cat).offset(skip).limit(limit).all()

def create_cat(db: Session, cat: CatCreate):
    db_cat = Cat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat 