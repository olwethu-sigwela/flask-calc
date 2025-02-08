import sqlite3
from flask import Flask, jsonify, request, make_response, render_template, url_for, flash, redirect
from flask_cors import CORS
from urllib.parse import urlparse
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

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
app.config["SECRET_KEY"] = "-6003720880522251805"
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
    conn = get_db_connection()
    calcs = conn.execute('SELECT * FROM calcs').fetchall()
    conn.close()
    return render_template("index.html", calcs=calcs)


# @app.route("/calc")
# def calc():
#     return render_template("calc.html")

@app.route("/calc" , methods = ['GET', 'POST'])
def do_calc():


    if request.method == "POST":
        # print(f"request={request}")
        # print(f"request.get_data() = {request.get_data(as_text=True)}")
        # print(f"type(request.get_data()) = {type(request.get_data(as_text=True))}")
        # print(f"request.get_data().split('\\n') = {request.get_data(as_text=True).split("\n")}")

        data = request.get_data(as_text=True).split("\n")
        x = int(request.form["x"])
        y = int(request.form["y"])
        op = request.form["operation"]

        if not(x and y and op):
            flash("Missing data!")
        else:

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



            calc = ops[op](x, y)

            full_op_names = {
                "add": "Add",
                "sub": "Subtract",
                "mul": "Multiply",
                "div": "Divide",
                "pow": "Power"
            }

            conn = get_db_connection()

            conn.execute("INSERT INTO calcs (x, y, operation, answer) VALUES (?, ?, ?, ?)", 
                         (x, y, full_op_names[op], float(calc)))
            
            conn.commit()
            conn.close()
            



        
            response = {
                "answer":calc
            }

            if calc != "ZeroDivisionError":
                response["message"] = "Calculation successful"
            else:
                response["message"] = "Calculation failed"

            return response

    return render_template("calc.html")

  


  


def main():
    app.run(host="0.0.0.0", port = 5000)



if __name__ == "__main__":
    main()



