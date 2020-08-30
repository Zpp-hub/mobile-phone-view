# -*- coding: utf-8 -*-
import traceback
from flask import Blueprint, jsonify
routes = Blueprint("info", __name__)


@routes.route("/test", methods=["GET"])
def get_user():
    result = {"statusCode": 1, "message": "ok", "data": None}
    try:
        result['data'] = '1234'
    except Exception as e:
        traceback.print_exc()
        result["code"] = -1
        result["message"] = str(e)
    return jsonify(result)







