import uvicorn
from fastapi import FastAPI

from db.database import db_init
from file import end_point

app = FastAPI(debug=True)

app.include_router(
    end_point.router,
    prefix="/api/v1/file",
    tags=["API для работы с файлами"],
)


db_init(app)  # Инициализация ДБ-схемы.


if __name__ == '__main__':
    uvicorn.run("application:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")