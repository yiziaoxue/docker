#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, abort, request, jsonify
from Controllers import test

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return test.index()


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)