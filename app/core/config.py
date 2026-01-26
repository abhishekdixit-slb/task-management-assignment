from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "TaskManager"
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    """
    Here, the lru_cache() is used to cache the settings object. 
    This is done to prevent the settings from being reloaded 
    every time the application is started. 
    Also, it returns the settings object, that contains all the configuration variables.
    """
    return Settings()