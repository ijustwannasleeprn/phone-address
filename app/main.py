from fastapi import FastAPI, HTTPException
from app.models import PhoneAddress
from app.redis_client import redis_client

app = FastAPI(
    title="AVE Technologies",
    description="Хранение адресов по номеру телефона",
    version="1.0.0"
)


@app.post("/write_data", response_model=PhoneAddress)
async def write_data(data: PhoneAddress):
    """
    Запись или обновление адреса по номеру телефона

    - **phone**: номер телефона
    - **address**: адрес
    """
    if not data.phone or not data.address:
        raise HTTPException(status_code=400, detail="Phone and address are required")

    redis_client.set_address(data.phone, data.address)
    return data


@app.get("/check_data")
async def check_data(phone: str):
    """
    Получение адреса по номеру телефона

    - **phone**: номер телефона
    """
    if not phone:
        raise HTTPException(status_code=400, detail="Phone is required")

    address = redis_client.get_address(phone)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found for this phone")

    return {"phone": phone, "address": address}
