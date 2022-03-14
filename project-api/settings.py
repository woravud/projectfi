from pydantic import BaseSettings


class Settings(BaseSettings):

    MODE: str = 'production'
    BASE_URL: str = 'http://localhost:8004'
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str = 'pg'
    DB_PORT: int = 5432
    DB_NAME: str

    class Config:
        env_file = '.env'


cfg: Settings = Settings()
