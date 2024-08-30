# Dockerfile
FROM python:3.12.5-slim

WORKDIR /mock

# Копируем файл requirements.txt из директории api
COPY ./api/requirements.txt . 

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы приложения в контейнер
COPY ./api/locust_mock.py .

# Запуск FastAPI приложения через uvicorn
CMD ["uvicorn", "locust_mock:app", "--host", "0.0.0.0", "--port", "8000"]
