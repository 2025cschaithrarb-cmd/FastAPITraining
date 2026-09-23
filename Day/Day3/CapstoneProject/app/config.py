#This file defines all configuration values the app needs
# (DB connection info, app name, etc)
#pydantic_settings: s: automatically reads environment variables and validates

from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    MONGO_URI : str = "mongodb://localhost:27017"
    MONGO_DB_NAME : str = "it_servicedesk"
    #Gives app name
    APP_NAME : str = "IT Service Desk App API"
    #Informs pydantic settings to read load values from .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
# Shared ssettings Object that all files can import
settings = Settings()