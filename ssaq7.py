history = []

def calculate(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b != 0 else "Error: Division by zero"

while True:
    action = input("Calculate (c), History (h), Quit (q): ")
    if action == 'c':
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))
        result = calculate(a, op, b)
        history.append(f"{a} {op} {b} = {result}")
        print(f"Result: {result}")
    elif action == 'h':
        print("Calculation History:")
        for calc in history:
            print(calc)
    elif action == 'q':
        break