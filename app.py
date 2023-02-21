from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home_page():
    return render_template("index.html")


# Receiving Data from Form
@app.route("/math", methods=['POST'])
def math_operation():
    if request.method == "POST":
        ops = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

        if ops == "add":
            r = num1 + num2
            res = f"The sum of {num1} and {num2} is {r}"

        if ops == "subtract":
            r = num1 - num2
            res = f"The difference of {num1} and {num2} is {r}"

        if ops == "multiply":
            r = num1 * num2
            res = f"The product of {num1} and {num2} is {r}"

        if ops == "divide":
            r = round(num1 / num2, 3)
            res = f"The division of {num1} and {num2} is {r}"
        return render_template("results.html", result=res)

    # Receiving Data from Postman


@app.route("/postman_data", methods=['POST'])
def math_operation1():
    if request.method == "POST":
        ops = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        if ops == "add":
            r = num1 + num2
            res = f"The sum of {num1} and {num2} is {r}"

        if ops == "subtract":
            r = num1 - num2
            res = f"The difference of {num1} and {num2} is {r}"

        if ops == "multiply":
            r = num1 * num2
            res = f"The product of {num1} and {num2} is {r}"

        if ops == "divide":
            r = round(num1 / num2, 3)
            res = f"The division of {num1} and {num2} is {r}"
        return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
