from typing import Optional

from file import models, schemas


class ServicesFile:
    schema = None

    def __init__(self, schema):
        self.schema = schema

    async def create_file(self) -> models.File:
        """Создаем объект модели File."""
        assert isinstance(self.schema, schemas.CreateFile), 'Schema is wrong format'
        return await models.File.create(file_path=self.schema.file_path, file_hash=self.schema.file_hash)

    @staticmethod
    async def get_file_by_file_hash(file_hash: str) -> Optional[models.File]:
        """Получаем объект модели File по хэшу файла."""
        return await models.File.filter(file_hash=file_hash).first()

    @staticmethod
    async def delete_file_by_file_hash(file_hash: str) -> None:
        """Удаляем объект модели File по хэшу файла."""
        await models.File.filter(file_hash=file_hash).delete()
