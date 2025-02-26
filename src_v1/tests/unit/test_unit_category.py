import pytest
from pydantic import ValidationError
from app.schemas.category_schema import (
    CategoryCreate
)

from app.models import Category
from fastapi import HTTPException
from tests.factories.models_factory import get_random_category_dict


def mock_output(return_value=None):
    return lambda *args, **kwargs:return_value

#
# @pytest.mark.unit_schema
# def test_unit_schema_category_validation():
#     valid_data = {'name': 'test_category',
#                   'slug': 'test_slug'}
#     category = CategoryCreate(**valid_data)
#     assert category.name == 'test_category'
#     assert category.is_activate is False
#     assert category.level == 100
#     invalid_data = {'name': 'test_category'}
#
#     with pytest.raises(ValidationError):
#         CategoryCreate(**invalid_data)


def test_unit_create_new_category_successfully(client, monkeypatch):
    category = get_random_category_dict()

    for key, value in category.items():
        monkeypatch.setattr(Category, key, value)
    monkeypatch.setattr('sqlalchemy.orm.Query.first', mock_output())
    monkeypatch.setattr('sqlalchemy.orm.Session.commit', mock_output())
    monkeypatch.setattr('sqlalchemy.orm.Session.refresh', mock_output())

    body = category.copy()
    body.pop('id')
    response = client.post('api/category', json=body)
    assert response.status_code == 201
    assert response.json() == category


@pytest.mark.parametrize('existing_category, category_data, expected_detail',
                          [
                              (True, get_random_category_dict(), 'Category with this name and level exists'),
                              (True, get_random_category_dict(), 'Category with this slug exists')
                          ])
# def test_unit_create_new_category_existing(client,
#                                            monkeypatch,
#                                            existing_category,
#                                            category_data,
#                                            expected_detail):
#     def mock_check_existing_category(db, category_data):
#         if existing_category:
#             raise HTTPException(status_code=400, detail=expected_detail)
#     monkeypatch.setattr('app.routers.category_router.check_existing_category', mock_check_existing_category,)
#     monkeypatch.setattr('sqlalchemy.orm.Query.first', mock_output())
#     body = category_data.copy()
#     body.pop('id')
#     response = client.post('/api/category/', json=body)
#     assert response.status_code == 400
#
#     if expected_detail:
#         assert response.json() == {'detail': expected_detail}
def test_unit_create_new_category_existing(
    client, monkeypatch, existing_category, category_data, expected_detail
):
    def mock_check_existing_category(db, category_data):
        if existing_category:
            raise HTTPException(status_code=400, detail=expected_detail)

    monkeypatch.setattr(
        "app.routers.category_router.check_existing_category",
        mock_check_existing_category,
    )

    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output())
    body = category_data.copy()
    body.pop("id")
    response = client.post("/api/category/", json=body)

    assert response.status_code == 400

    if expected_detail:
        assert response.json() == {"detail": expected_detail}


def test_unit_create_new_category_with_internal_server_error(client, monkeypatch):
    category = get_random_category_dict()

    def mock_create_category_exception(*args, **kwargs):
        raise Exception("Internal server error")

    for key, value in category.items():
        monkeypatch.setattr(Category, key, value)
    monkeypatch.setattr('sqlalchemy.orm.Query.first', mock_output())
    monkeypatch.setattr('sqlalchemy.orm.Session.commit', mock_create_category_exception)

    body = category.copy()
    body.pop("id")
    response = client.post("api/category/", json=body)
    assert response.status_code == 500

