
class Fibonacci_Iter():
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_a = self.a
        if self.count == self.limit:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return current_a

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        count += 1
        a, b = b, a + b

def fibonacci_method(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        print(a)
        count += 1
        a, b = b, a + b

def fibonacci_lambda(limit):
    fib = lambda n: n if n <= 1 else (fib(n - 1) + fib(n - 2))
    return fib(limit)


print("===fibonacci_generator===")
for n in fibonacci_generator(10):
    print(n)

print("===fibonacci_iteration===")
for obj in Fibonacci_Iter(10):
    print(obj)

print("===fibonacci_method===")
fibonacci_method(10)

print("===fibonacci_lambda===")
print(fibonacci_lambda(10))

