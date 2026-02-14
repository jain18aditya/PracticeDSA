"""
Problem: Fibonacci Sequence — Multiple Implementations

Implement different ways to generate Fibonacci numbers up to a given limit.

The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2)  for n >= 2

Example:
Input: limit = 10
Output: 0 1 1 2 3 5 8 13 21 34

Tasks:

1. Generator Approach
   - Implement a generator function that yields Fibonacci numbers one by one.
   - Should be memory efficient using `yield`.

2. Iterator Class Approach
   - Implement a custom iterator class using:
        __iter__()
        __next__()
   - Should behave like a built-in iterable.

3. Iterative Method
   - Implement a simple method that prints Fibonacci numbers using a loop.

4. Recursive (Lambda) Approach
   - Implement Fibonacci using recursion.
   - Return the nth Fibonacci number.

Requirements:

- Input: integer `limit` (number of Fibonacci values to generate)
- Output:
    - Generator → yields sequence
    - Iterator → iterable sequence
    - Method → prints sequence
    - Lambda → returns nth Fibonacci number

Constraints:
- 0 <= limit <= 10^5 for iterative/generator approaches
- Recursive approach is inefficient for large `n` (exponential time)
"""

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

