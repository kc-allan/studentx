from flask import Flask
from config import config
from fastapi import FastAPI
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.middleware.proxy_fix import ProxyFix
from starlette.middleware.wsgi import WSGIMiddleware

from app.api import apiApp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    fastapi_wsgi_app = WSGIMiddleware(apiApp)

    # Initialize extensions here
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/api': fastapi_wsgi_app
    })

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1,
                            x_host=1, x_port=1, x_proto=1)

    # Attach blueprints here

    # Attach shell context processors here

    # Attach request context processors here

    # Attach error handlers here

    # Attach before and after request handlers here

    return app
