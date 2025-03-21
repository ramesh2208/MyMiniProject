from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.form['expression']

        # Replace square root symbol (√) with proper function calls
        expression = re.sub(r'math\.sqrt\((\d+(\.\d+)*)\)', r'math.sqrt(\1)', expression)

        # Evaluate expression securely
        result = eval(expression, {"__builtins__": None}, {"math": math})

        # Return absolute value of result
        return jsonify(result=str(abs(result)))  # Ensure positive output

    except Exception:
        return jsonify(error="Invalid Input or Operation")

if __name__ == '__main__':# This code only runs if the script is executed directly
    # name__ is a special variable set to "__main__" when the script is run directly.
    app.run(debug=True)
