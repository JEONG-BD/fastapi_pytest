from sqlalchemy import Integer, Boolean, String


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("category")


def test_model_structure_column_data_types(db_inspector):
    table = "category"
    columns = {columns['name'] : columns for  columns in db_inspector.get_columns(table)}
    print(columns)

    assert isinstance(columns['id']['type'], Integer)
    assert isinstance(columns['name']['type'], String)
    assert isinstance(columns['slug']['type'], String)
    assert isinstance(columns['is_activate']['type'], Boolean)
    assert isinstance(columns['level']['type'], Integer)
    assert isinstance(columns['parent_id']['type'], Integer)