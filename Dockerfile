FROM python:3.12.5-slim
WORKDIR /mock
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["unicorn", "locust_mock:app", "-host", "0.0.0.0", "-port", "8000"]