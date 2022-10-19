from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'C394Eb5iosnH7ppFmcxO1Cyc1TA4D2Rjjop0ppevRCg'
    ALGORITHM: str = 'HS256'
    # expira em 1 semana = 60 minutos * 24 horas * 7 dias
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 

    class Config:
        case_sensitive = True


settings: Settings  = Settings()
