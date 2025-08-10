def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

try:
    n = int(input("Enter number of Fibonacci numbers: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
except ValueError:
    print("Please enter a valid integer!")