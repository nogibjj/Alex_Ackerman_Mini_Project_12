from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the calculator
calculator_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="POST">
        <label for="num1">Number 1:</label>
        <input type="number" name="num1" id="num1" required>
        <br><br>
        <label for="num2">Number 2:</label>
        <input type="number" name="num2" id="num2" required>
        <br><br>
        <label for="operation">Operation:</label>
        <select name="operation" id="operation" required>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>
        <br><br>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Retrieve form data
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            # Perform calculation based on selected operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero!"
        except ValueError:
            result = "Error: Invalid input!"

    # Render the template with the result
    return render_template_string(calculator_template, result=result)


if __name__ == "__main__":
    app.run(debug=True)
