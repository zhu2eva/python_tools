# coding: utf-8
import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_executor import Executor

from app.api import bp as poscar_bp
from app.errors import bp as errors_bp
from config import Config

db = SQLAlchemy()
migrate = Migrate()
executor = Executor()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
    executor.init_app(app)
    app.register_blueprint(poscar_bp)
    app.register_blueprint(errors_bp)
    if not app.debug and not app.testing:
        log_directory = app.config['LOG_DIRECTORY']
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        file_handler = RotatingFileHandler(os.path.join(log_directory, 'app.log'), maxBytes=1024000, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('mci-connector-vasp startup')
    return app
