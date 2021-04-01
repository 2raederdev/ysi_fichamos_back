# -*- coding: utf-8 -*-

import os
import importlib

import flask
from werkzeug.exceptions import HTTPException

def register_blueprints(app: flask.Flask):
    # Register all blueprints in ./src/blueprints folder:
    # The blueprint name should be the same as filename + the '_bp' suffix
    # Example, for './src/blueprints/test.py' file, the blueprint variable name should be 'test_bp':
    #   test_bp = flask.Blueprint('test', __name__, url_prefix='/prefix_path...')
    try:
        for root, dirs, files in os.walk("./src/blueprints"):
            for filename in files:
                if not filename.startswith('__') and filename.endswith('.py'):
                    bp_name = filename.replace('.py', '')
                    bp = importlib.import_module(f'src.blueprints.{bp_name}')
                    app.register_blueprint(getattr(bp, f'{bp_name}_bp'))
    except Exception as e:
        print(e)