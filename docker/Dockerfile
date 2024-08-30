FROM python:3.12.5-slim

WORKDIR /mock

COPY ./api/requirements.txt . 
RUN pip install -r requirements.txt
COPY ./api/locust_mock.py .  

CMD ["uvicorn", "locust_mock:app", "--host", "0.0.0.0", "--port", "8000"]

