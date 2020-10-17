import os
from typing import IO, Optional

from file import schemas, models
from file.service import ServicesFile
from file.utils import get_file_hash, save_file, initialize_file_path_in_os


async def create_file(file: IO, file_name: str) -> str:
    """
    Создает объект модели File и сохраняет сам файл в ОС.

    :param file: Файл в двоичном представлении.
    :param file_name: Название загружаемого файла, в формате: "название.расширение"
    :return: Хэш файла.
    """
    file_hash = get_file_hash(file)  # Получаем хэш файла.

    file_path_in_os = initialize_file_path_in_os(file_hash=file_hash)   # Инициализируем путь, куда будет сохр-н. файл.

    file_type = file_name.split('.')[-1]  # Получаем расширение файла (тип).
    new_file_name = f'{file_hash}.{file_type}'  # Формируем новое имя файла на основе полученного хэша.
    # Сохраняем файл в инициализированную директорию и получаем полный путь до файла в ОС.
    full_file_path_in_os = save_file(file=file, file_name=new_file_name, file_dir=file_path_in_os)

    schema = schemas.CreateFile(file_hash=file_hash, file_path=full_file_path_in_os)
    await ServicesFile(schema).create_file()  # Создаем объект модели File с данными о хэше файла и пути к нему.

    return file_hash  # Возвращаем хэш.


async def get_full_file_path_in_os_by_hash(file_hash: str) -> Optional[str]:
    """
    Получаем полный путь к файлу в ОС по хэшу.

    :param file_hash: Хэш файла.
    :return: Если файл был загружен, то возвращает полный путь к файлу в ОС, иначе возвращает None.
    """
    file = await ServicesFile.get_file_by_file_hash(file_hash=file_hash)  # Получаем объект модели File с данными.
    if not file:  # Объект модели не будет получен в случае, если файл не был загружен ранее.
        return None

    return file.file_path  # Возвращаем полный путь к файлу в ОС.


async def delete_file_in_os(file: models.File) -> None:
    """Удаляет файл из ОС, а также объект модели File с данными о нем."""
    file_path_in_os = file.file_path  # Получаем полный путь к файлу в ОС.
    os.remove(file_path_in_os)  # Удаляем файл по указанному пути. Директория не удаляется.
    await ServicesFile.delete_file_by_file_hash(file_hash=file.file_hash)  # Удаляем объект модели File.
