from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from urllib.parse import urlparse


class Calc:
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y
    
    @staticmethod
    def mul(x, y):
        return x * y
    
    @staticmethod
    def pow(x, y):
        return x**y
    
    @staticmethod
    def div(x, y):
        if y != 0:
            return x/y
        
        return ZeroDivisionError
    
app = Flask(__name__)

@app.route('/add', methods = ['POST'])
def mine():
    values = request.get_json()

    required = ['x', 'y']

    if not all(k in values for k in required):
        return "Missing values", 400
    
    x = values["x"]
    y = values["y"]

    print(f"x = {x} type(x) = {type(x)}")

    
