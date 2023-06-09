from decouple import config
import os 


class DevConfig:
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast = bool)
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
