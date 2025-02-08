from flask import Flask, jsonify, request, make_response, render_template
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
        
        return "ZeroDivisionError"
    
app = Flask(__name__)

@app.route('/add', methods = ['POST'])
def add():
    values = request.get_json()

    required = ['x', 'y']

    if not all(k in values for k in required):
        return "Missing values", 400
    
    x = values["x"]
    y = values["y"]

    response = {
        "message": "Calculation successful",
        "answer": Calc.add(x, y)
       
    }

    return jsonify(response), 200

@app.route('/sub', methods = ['POST'])
def sub():
    values = request.get_json()
    required = ['x', 'y']

    if not all(k in values for k in required):
        return "Missing values", 400
    
    x = values['x']
    y = values['y']

    response = {
        "message": "Calculation successful",
        "answer": Calc.sub(x, y)
    }

    return response

@app.route('/mul', methods = ['POST'])
def mul():
    values = request.get_json()
    required = ['x', 'y']

    if not all(k in values for k in required):
        return "Missing values", 400
    
    x = values['x']
    y = values['y']

    response = {
        "message": "Calculation successful",
        "answer": Calc.mul(x, y)
    }

    return response

@app.route('/div', methods = ['POST'])
def div():
    values = request.get_json()
    required = ['x', 'y']

    if not all(k in values for k in required):
        return "Missing values", 400
    
    x = values['x']
    y = values['y']
    calc = Calc.div(x, y)

    response = {
        "answer": calc
    }

    if calc == "ZeroDivisionError":
        response["message"] = "Calculation failed"
    else:
        response["message"] = "Calculation successful"

    return response



@app.route('/pow', methods = ['POST'])
def pow():
    values = request.get_json()
    required = ['x', 'y']

    if not all(k in values for k in required):
        return "Missing values", 400
    
    x = values['x']
    y = values['y']

    response = {
        "message": "Calculation successful",
        "answer": Calc.pow(x, y)
    }

    return response

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc")
def calc():
    return render_template("calc.html")

@app.route("/do_calc" , methods = ['POST'])
def do_calc():

    # print(f"request={request}")
    # print(f"request.get_data() = {request.get_data(as_text=True)}")
    # print(f"type(request.get_data()) = {type(request.get_data(as_text=True))}")
    # print(f"request.get_data().split('\\n') = {request.get_data(as_text=True).split("\n")}")

    data = request.get_data(as_text=True).split("\n")
    x = int(data[3])
    y = int(data[7])
    op = data[11].strip("\r")

    # print(f"x = {x}")
    # print(f"y = {y}")
    # print(f"op = {op}")
    # print(f"x == 3 = {x == 3}")
    # print(f"y == 5 = {y == 5}")
    # print(f"op == 'div' = {op == "div"}")

    # values = request.get_json()

    # print(f"values = {values}")

    ops = {
        "add": Calc.add,
        "sub": Calc.sub,
        "mul": Calc.mul,
        "div": Calc.div,
        "pow": Calc.pow
    }

    calc = ops[op]


 
    response = {
        "answer":calc
    }

    if calc != "ZeroDivisionError":
        response["message"] = "Calculation successful"
    else:
        response["message"] = "Calculation failed"

    return response

  


  


def main():
    app.run(host="0.0.0.0", port = 5000)



if __name__ == "__main__":
    main()



