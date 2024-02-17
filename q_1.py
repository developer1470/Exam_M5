def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_generator = fib()

for _ in range(10):
    print(next(fibonacci_generator))
