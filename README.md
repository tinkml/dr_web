## Технологии:
- FastAPI
- Tortoise ORM
- Docker

## Необходимо, чтобы были установленны:
- <a href="https://www.docker.com/get-started">Docker/a>
- <a href="https://docs.docker.com/compose/install/">Docker Compose</a>
- <a href="https://github.com/">GitHub</a>

## Чтобы начать использовать:
Склонируйте репозиторий с проектом:
```sh
git clone https://github.com/tinkml/haclever.git
```

Перейдите в директорию проекта:
```sh
cd dr_web
```

Сформируйте .env файлы на основе .env.example.
```sh
https://docs.google.com/document/d/1nL8otZAJWVy7jKCArMyzYs3jY2WoihSZsYANLbNtbA0/edit?usp=sharing
```

Запустите процесс сбоки контейнеров с помощью docker-compose:
```sh
docker-compose up -d --build
```

Проект станет доступен по адресу 
```sh
http://0.0.0.0:8000//docs
```

## Важно:
Если у вас на компьютере установлен PostgresQL.
- Проверьте, статус
```sh
sudo systemctl status postgresql
```
- Если статус "active", становите процесс
```sh
sudo systemctl stop postgresql
```
