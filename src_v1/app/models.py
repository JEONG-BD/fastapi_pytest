from app.db_connection import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    CheckConstraint
)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    is_activate = Column(Boolean, nullable=False, default=False, server_default='False')
    level = Column(Integer, nullable=False, default='100', server_default='100')
    parent_id = Column(Integer, nullable=True)

    __table_args__ = (
        CheckConstraint('LENGTH(name) > 0', name='name_length_check'),
        CheckConstraint('LENGTH(slug) > 0', name='slug_length_check'),
    )
