def calculate(a: float, b: float, operation: str = "add"):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b if b != 0 else "Cannot divide by zero"
    return {"a": a, "b": b, "operation": operation, "result": result}