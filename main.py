# coding:utf-8
from flask import Flask
import router
import platform

app = Flask(__name__)

router.register(app)

if __name__ == '__main__':
    # 根据实际情况修改端口号
    os_ = platform.platform()
    if os_.startswith("Windows"):
        app.run()
    else:
        app.run(host="0.0.0.0", port=8041, threaded=False, debug=True)
