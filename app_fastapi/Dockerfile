FROM python:3.11

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app_fastapi /app_fastapi/
COPY .env .env


CMD ["uvicorn", "app_fastapi.app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]