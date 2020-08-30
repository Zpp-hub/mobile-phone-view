# coding:utf-8
from flask import Blueprint, jsonify
from . import info_rt

bp = Blueprint('router', __name__)

def register(app):
    @app.route('/')
    def default_router():
        return jsonify({"statusCode":1,"message":"ok","data":None})

    app.register_blueprint(info_rt.routes, url_prefix='/api/info')






