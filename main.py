# coding:utf-8
from flask import Flask
import router

app = Flask(__name__)

router.register(app)

if __name__ == "__main__":
    app.run()

