from app.db_connection import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    slug = Column(String(100))
    is_activate = Column(Boolean)
    level = Column(Integer)
    parent_id = Column(Integer)
