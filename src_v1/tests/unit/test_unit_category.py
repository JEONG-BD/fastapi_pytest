import pytest
from pydantic import ValidationError
from app.schemas.category_schema import (
    CategoryCreate
)


@pytest.mark.unit_schema
def test_unit_schema_category_validation():
    valid_data = {'name': 'test_category',
                  'slug': 'test_slug'}
    category = CategoryCreate(**valid_data)
    assert category.name == 'test_category'
    assert category.is_activate is False
    assert category.level == 10
    invalid_data = {'name': 'test_category'}

    with pytest.raises(ValidationError):
        CategoryCreate(**invalid_data)