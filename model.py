from database import Base
from sqlalchemy import Column, Integer, String

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
