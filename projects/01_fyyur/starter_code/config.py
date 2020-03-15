from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://fyuur:fyuur@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database

engine = create_engine(SQLALCHEMY_DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)


#print(database_exists(engine.url))


