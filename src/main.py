import asyncio

from src.config import config
from src.exception import APIException, HTTPException
from src.kavenegar import KavenegarAPI


async def send_sms():
    api: KavenegarAPI = KavenegarAPI(apikey=config.KAVENEGAR_API_KEY)
    params: dict = {
        "sender": config.SENDER_NUMBER,
        "receptor": config.RECEPTOR_NUMBER,
        "message": "Test kavenegar message.",
    }

    try:
        response = await api.sms_send(params=params)
        print("SMS Sent Successfully:", response)
    except APIException as e:
        print(f"APIException occurred: {e}")
    except HTTPException as e:
        print(f"HTTPException occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(send_sms())
