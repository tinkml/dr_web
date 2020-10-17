import os

POSTGRES_DB = os.environ.get("POSTGRES_DB", 'dr_web')
POSTGRES_USER = os.environ.get("POSTGRES_USER", 'dr')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", '124356')
POSTGRES_CONTAINER_NAME = os.environ.get("POSTGRES_CONTAINER_NAME", "localhost")
