from fastapi import FastAPI, Request, HTTPException
import random

app = FastAPI()

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
