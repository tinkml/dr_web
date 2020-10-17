import os


def check_url(url: str) -> None:
    """Проверка пути в случае если пути к директории нет создает его."""
    if not os.path.exists(url):
        os.makedirs(url)
