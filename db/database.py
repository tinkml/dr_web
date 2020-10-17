from tortoise.contrib.fastapi import register_tortoise

from db.settings import (
    POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_CONTAINER_NAME,

)


# DATABASE_URL = postgresql+psycopg2://{user}:{password}@{host}:{port}
POSTGRES_DATABASE_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_CONTAINER_NAME}:5432/{POSTGRES_DB}'


MODELS_LIST = [
    "file.models"
]

# Необходимо для мигратора aerich
TORTOISE_ORM = {
    "connections": {"default": POSTGRES_DATABASE_URL},
    "apps": {
        "models": {
            "models": MODELS_LIST,
            "default_connection": "default",
        },
    },
}


def db_init(app):
    """Инициализация схемы-БД."""
    register_tortoise(
        app,
        db_url=POSTGRES_DATABASE_URL,
        modules={"models": MODELS_LIST},
        generate_schemas=True,
        add_exception_handlers=True,
    )
