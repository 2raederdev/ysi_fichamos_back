# -*- coding: utf-8 -*-

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    PORT = os.getenv('PORT')
