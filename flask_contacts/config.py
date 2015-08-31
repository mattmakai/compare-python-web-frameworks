import os


DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
