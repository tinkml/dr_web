import mmap
from hashlib import sha512
from os.path import join
from typing import IO

from common.utils import check_url
from settings import FILE_STORAGE_PATH


def get_file_hash(file: IO) -> str:
    """Получение хэш-суммы файла."""
    hash = sha512()  # Получаем объект на основе алгоритма SHA512, из которого будет сформирован хэш.

    # Подробнее о mmap: https://docs.python.org/3/library/mmap.html
    # Позволяет работать с файлом, как с строкой байтов.
    with mmap.mmap(fileno=file.fileno(), length=0, prot=mmap.PROT_READ) as mm:
        hash.update(mm)  # Передаем последовательность байтов файла в объект hash.

    return hash.hexdigest()  # Возвращаем зашифрованную строку (хэш).


def save_file(file: IO, file_name: str, file_dir: str) -> str:
    """
    Сохраняет файл в указанную лиректорию.

    :param file: Файл в двоичном представлении.
    :param file_name: Название загружаемого файла, в формате: "хэш.расширение"
    :param file_dir: Путь к директории в ОС, куда будет сохранен файл.
    :return: Полный путь к файлу в ОС.
    """
    file_path = join(file_dir, file_name)  # Полный путь к файлу в ОС.

    # Записываем файл по укзанному пути.
    with open(file_path, 'wb+') as file_in_os:
        file_in_os.write(file.read())

    return file_path  # Возвращаем полный путь к файлу в ОС.


def initialize_file_path_in_os(file_hash: str) -> str:
    """Создаем директорию, где будет храниться загружаемый файл."""
    file_directory = file_hash[:2]  # Формируем название директории на основе хэша.
    file_path_in_os = f'{FILE_STORAGE_PATH}{file_directory}'  # Путь к директории в ОС.
    check_url(file_path_in_os)  # Проверяем, существует ли такая директория, если нет - создаем.
    return file_path_in_os  # Возвращаем путь к директории в ОС.
