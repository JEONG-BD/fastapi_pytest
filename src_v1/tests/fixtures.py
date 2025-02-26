import os
import pytest
from sqlalchemy import create_engine
from tests.utils.docker_utils import start_database_container
from tests.utils.database_utils import migrate_to_db
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import  TestClient
from main import app


@pytest.fixture(scope="session")
def db_session():
    print("1=========")
    container = start_database_container()

    engine = create_engine(os.getenv("TEST_DATABASE_URL"))

    with engine.begin() as connection:
        migrate_to_db("migrations", "alembic.ini", connection)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    yield SessionLocal

    # container.stop()
    # container.remove()
    # engine.dispose()


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as _client:
        yield _client
    # container.stop()
    # container.remove()
    # engine.dispose()gb
