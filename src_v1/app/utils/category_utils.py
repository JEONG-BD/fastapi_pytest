from fastapi import  HTTPException
from app.db_connection import get_db_session, SessionLocal
from app.models import Category
from app.schemas.category_schema import (
    CategoryReturn,
    CategoryCreate
)
from sqlalchemy.orm import Session


def check_existing_category(db: Session, category_data: CategoryCreate):
    existing_category = (
        db.query(Category)
        .filter((Category.slug == category_data.slug) |
               (Category.name == category_data.name) &
               (Category.level == category_data.level)).first()
    )

    if existing_category:
        if (existing_category.name == category_data.name and
                existing_category.level == category_data.level):

            detail_msg = 'Category with this name and level exists'
        else:
            detail_msg = 'Category slug already exists'

        raise HTTPException(status_code=400, detail=detail_msg)

