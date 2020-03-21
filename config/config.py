import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'some string'
    APP_NAME = 'cft'
    MONGODB_SETTINGS = {'DB': 'cft'}
