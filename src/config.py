import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEFAULT_TIMEOUT: int = 10

    KAVENEGAR_API_KEY: str = os.getenv("KAVENEGAR_API_KEY")
    SENDER_NUMBER: str = os.getenv("SENDER_NUMBER")
    RECEPTOR_NUMBER: str = os.getenv("RECEPTOR_NUMBER")


config: Config = Config()
