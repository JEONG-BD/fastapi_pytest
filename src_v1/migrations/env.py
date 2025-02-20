import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app import models
config = context.config

url_db1 = os.environ.get("DEV_DATABASE_URL")
url_db2 = os.environ.get("TEST_DATABASE_URL")
# print(url_db1, url_db2)
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)
# print("*"*20)
# if os.environ.get("DEV_DATABASE_URL") is not None:
#     config.set_section_option("devdb", "sqlalchemy.url", os.environ.get("DEV_DATABASE_URL"))
# print("*"*20)
# if os.environ.get("TEST_DATABASE_URL") is not None:
#     config.set_section_option("devtest", "sqlalchemy.url", os.environ.get("TEST_DATABASE_URL"))
# print("*"*20)


# Modify the database URLs in the Alembic config
config.set_section_option("devdb", "sqlalchemy.url", url_db1)
config.set_section_option(
    "devtest", "sqlalchemy.url", os.environ.get("TEST_DATABASE_URL")
)

target_metadata = models.Base.metadata


def run_migrations_offline() -> None:

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
