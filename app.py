from flask import Flask, render_template, request
import math

app = Flask(__name__)

def find_number_in_pi(number):
    pi_digits = str(math.pi)
    position = pi_digits.find(number)
    return position

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_pi", methods=["POST"])
def check_pi():
    number = request.form.get("number")
    position = find_number_in_pi(number)
    if position != -1:
        return "The number {} is found at position {}".format(number, position)
    else:
        return "The number {} is not found in the digits of Pi.".format(number)

if __name__ == "__main__":
    app.run(debug=True)
