from fastapi import FastAPI, Request, HTTPException
from prometheus_client import Counter, Histogram, make_asgi_app
import random
import time

app = FastAPI()

#общее число запросов
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'http_status'])
#время отклика
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency', ['endpoint'])

#экспорт метрик в /metrics
metrics_app = make_asgi_app()
#монтирование в FastAPI
app.mount("/metrics", metrics_app)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    #время на обработку запросов
    process_time = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(process_time)
    #увеличение счетчика
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path, http_status=response.status_code).inc()
    return response

@app.get("/login/{username}")
async def login(username: str):
    return {"token": f"Token_{username}"}

@app.post("/booking/add")
async def add_booking(request: Request):
    try:
        #получить данные запроса в формате JSON
        booking_data = await request.json()
        service_name = booking_data.get("service_name")
        
        #проверка, что 'service_name' есть и не пустой
        if not service_name:
            raise HTTPException(status_code=400, detail="Service name is required")

        #успешные сообщения
        response_messages = [
            f"Услуга '{service_name}' забронирована! Готовьтесь к приключениям!",
            f"Ой! Услуга '{service_name}' сейчас на каникулах. Попробуйте выбрать что-то другое.",
            f"'{service_name}' успешно забронирована. Надеемся, у вас нет аллергии!",
            f"Не удалось забронировать '{service_name}'. Виноваты гремлины в системе.",
            f"'{service_name}' забронирована. Возвратов нет, но и сожалений тоже!"
        ]
        return {"message": random.choice(response_messages)}

    except Exception as e:
        #логирование ошибок 
        print(f"Error in /booking/add: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/checkout")
async def checkout(request: Request):
    try:
        checkout_data = await request.json()
        return {"message": "Покупка успешно завершена! Время праздновать... или вздремнуть."}
    except Exception as e:
        print(f"Error in /checkout: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
