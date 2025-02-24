from app.db_connection import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    is_activate = Column(Boolean, nullable=False)
    level = Column(Integer, nullable=False)
    parent_id = Column(Integer, nullable=True)
