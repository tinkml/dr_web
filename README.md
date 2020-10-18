## Технологии:
- FastAPI
- Tortoise ORM

## Необходимо, чтобы были установленны:
- <a href="https://www.python.org/downloads/">Python 3.8.3</a>
- <a href="https://www.postgresql.org/download/">PostgresQL</a>
- <a href="https://github.com/">GitHub</a>

## Чтобы начать использовать:
1.Склонируйте репозиторий с проектом:
```sh
git clone https://github.com/tinkml/haclever.git
```

2.Создайте БД и пользователя в PostgresQL

3.Перейдите в директорию проекта:
```sh
cd dr_web
```

4.Создайте виртуальное окружение Python и активируйте его.
```sh
python -m venv venv
source env/bin/activate - for Linux.
env\Scripts\activate - for Windows.
```

5.Установите все необходимые зависимости:
```sh
pip3 install -r req.txt - for Linux
pip install -r req.txt - for Windows
```

6.Запустите проект:
```sh
python3 application.py - for Linux
python application.py - for Windows
```


Проект станет доступен по адресу 
```sh
http://0.0.0.0:8000//docs
```

## Важно:
- Проеверьте, создан ли пользователь и база данных в PostgresQL
- Настройка и инифиализация БД находится в директории db/
