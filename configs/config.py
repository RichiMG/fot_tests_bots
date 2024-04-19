import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

@dataclass
class DataclassConfig:
    databasse: str
    db_host: str
    db_user: str
    db_password: str

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot
    db: DataclassConfig

env= load_dotenv(find_dotenv())

def strt_config(patch: str|None)->Config:
    return Config(
        tg_bot=TgBot(
            token=os.getenv("bot_token"),
            admin_ids=(list(map(int, os.getenv('admins_lst'))))
        ),
        db=DataclassConfig(
            databasse=os.getenv('DATABASE'),
            db_host=os.getenv('DB_HOST'),
            db_user=os.getenv('DB_USER'),
            db_password=os.getenv('DB_PASSWORD')
        )
    )