from sqlalchemy.orm import Session
from server.database.models.cat import Cat
from server.schemas.cat import CatCreate

def get_cats(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cat).offset(skip).limit(limit).all()

def get_cat(db: Session, cat_id: int):
    return db.query(Cat).filter(Cat.id == cat_id).first()

def create_cat(db: Session, cat: CatCreate):
    db_cat = Cat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_cat(db: Session, cat_id: int, cat: CatCreate):
    db_cat = get_cat(db, cat_id)
    if db_cat:
        for key, value in cat.dict().items():
            setattr(db_cat, key, value)
        db.commit()
        db.refresh(db_cat)
    return db_cat

def delete_cat(db: Session, cat_id: int):
    db_cat = get_cat(db, cat_id)
    if db_cat:
        db.delete(db_cat)
        db.commit()
    return db_cat 