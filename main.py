# -*- coding: utf-8 -*-

import src
import os
from flask import Flask, request, jsonify
from config import Config
from src.setup import register_blueprints
from src.exceptions.response_exceptions import ResponseBaseException


# from src.services.db import init_db


app = Flask(src.__name__)
app.config.from_object(Config())


@app.errorhandler(ResponseBaseException)
def handle_response_exceptions(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# @app.route('/')
# def hello():
#     return 'Hola amigo!!!'


# if __name__ == "__main__":
#     app.run(port=5000,debug=True)

# Setup
register_blueprints(app)