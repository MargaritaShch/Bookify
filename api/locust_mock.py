from fastapi import FastAPI, Request
import random
import json

#экземпляр FastAPI-приложения
app = FastAPI()

#эндпоинт для авторизации пользователя
@app.get("/login/{username}")
async def login(username: str):
    #возврат JSON-ответ с токеном(из имени пользователя)
    return {"token": f"Token_{username}"}

#эндпоинт для добавления бронирования
@app.post("/booking/add")
async def add_boking(request: Request):
    #получить данные запрсоа в формате JSON
    booking_data =  await request.json()
    srvice_name = booking_data.get("srvice_name")
    #успешные сообщения
    response_messages = [
        f"Услуга '{srvice_name}' забронирована! Готовьтесь к приключениям!",
        f"Ой! Услуга '{srvice_name}' сейчас на каникулах. Попробуйте выбрать что-то другое.",
        f"'{srvice_name}' успешно забронирована. Надеемся, у вас нет аллергии!",
        f"Не удалось забронировать '{srvice_name}'. Виноваты гремлины в системе.",
        f"'{srvice_name}' забронирована. Возвратов нет, но и сожалений тоже!"
    ]
    #возврат рандомного сообщения
    return {"message": random.choice(response_messages)}

@app.post("/checkout")
async def checkout(request: Request):
    checkout_data = await request.json()
    return {"message": "Покупка успешно завершена! Время праздновать... или вздремнуть."}