from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

from file import logic
from file.service import ServicesFile

router = APIRouter()


@router.post('/upload_file_in_os')
async def upload_file_in_os(file: UploadFile = File(...)) -> str:
    """Загрузка файла в ОС."""
    # Получаем хэш файла. Сохраняем файл в ОС.
    return await logic.create_file(file=file.file, file_name=file.filename)  # Получаем хэш файла. Сохраняем файл в ОС.


@router.get('/download_file_from_os/{file_hash}')
async def download_file_from_os(file_hash: str) -> FileResponse:
    """Получение файла из ОС хэш."""

    full_file_path_in_os = await logic.get_full_file_path_in_os_by_hash(file_hash=file_hash)  # Полный путь к файлу в ОС
    if not full_file_path_in_os:
        raise HTTPException(status_code=501, detail="File is not found")

    return FileResponse(path=full_file_path_in_os)  # Возвращаем файл.


@router.delete('/delete_file_in_os/{file_hash}')
async def download_file_from_os(file_hash: str) -> None:
    """Удаление файла из ОС по хэш."""
    file = await ServicesFile.get_file_by_file_hash(file_hash=file_hash)  # Получ-м объект модели File c данными о файле
    if not file:
        raise HTTPException(status_code=501, detail="File is not found")

    await logic.delete_file_in_os(file=file)  # Удаляем файл из ОС  данные о нем из БД.


