import os 
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)


class Settings:
    PROJECT_NAME:str = "proyecto fast-api"
    PROJECT_VERSION:str = "1.0"
    POSTGRES_DB:str = os.getenv('POSTGRES_DB')
    POSTGRES_USER:str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT:str = os.getenv('POSTGRES_PORT')
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Aprend1z.22@localhost/postgres"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

settings = Settings()
"postgresql://postgres:Aprend1z.22@localhost/postgres"
print(settings.DATABASE_URL)
