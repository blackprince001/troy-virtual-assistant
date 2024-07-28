from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "TROY Virtual Teaching Assistant"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MODEL_MAX_LENGTH: int = 100

    class Config:
        env_file = ".env"


settings = Settings()
