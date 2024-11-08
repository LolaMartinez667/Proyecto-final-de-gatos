from pydantic import BaseModel

class CatBase(BaseModel):
    name: str
    age: int
    breed: str
    personality: str

class CatCreate(CatBase):
    pass

class Cat(BaseModel):
    id: int
    name: str
    age: int
    breed: str
    personality: str

    class Config:
        from_attributes = True 