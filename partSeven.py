def perform_operation(num1, num2, operation):
   
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        case "^":
            return num1 ** num2
        case "%":
            return num1 % num2
        case _:
            return "Invalid operation. Please use +, -, *, /, ^, or %."

def calculator():
    print("Type 'quit' to exit.")
    while True:
        calculator_input = input("Enter two numbers and an operation: ")
        if calculator_input.lower() == "quit":
            print("Quitting the application.")
            break
        parts = calculator_input.split()
        if len(parts) != 3:
            print("Please provide exactly two numbers and an operation.")
            continue
        try:
            num1, num2, operation = float(parts[0]), float(parts[1]), parts[2]
            result = perform_operation(num1, num2, operation)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter two valid numbers followed by an operation.")


calculator()