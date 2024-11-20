from sqlalchemy import Column, Integer, String
from server.database.database import Base

class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    breed = Column(String)
    personality = Column(String) 