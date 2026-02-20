"""
Evaluate a mathematical expression string containing:

Non-negative integers (multi-digit allowed)

Operators: +, -, *, /

No parentheses

Division is integer division truncating toward zero

Expression may start with a negative number

No invalid character
Input:  "4+11-5*4+6/3-2"
Output: -5

Input:  "-4+2"
Output: -2
"""
# 4+1-5*4+6/3-2 = -15
def evaluate_expression(s: str) -> int:
    if not s:
        raise ValueError("Empty expression")

    stack = []
    num = 0
    operation = '+'

    for i, ch in enumerate(s):

        # Build number (multi-digit)
        if ch.isdigit():
            num = num * 10 + int(ch)

        # If operator OR last character → evaluate previous operator
        if ch in "+-*/" or i == len(s) - 1:

            if operation == '+':
                stack.append(num)

            elif operation == '-':
                stack.append(-num)

            elif operation == '*':
                stack.append(stack.pop() * num)

            elif operation == '/':
                if num == 0:
                    raise ZeroDivisionError("Division by zero")
                # truncate toward 0 (important for interview correctness)
                stack.append(int(stack.pop() / num))

            operation = ch
            num = 0

    return sum(stack)

print(evaluate_expression("4+11-5*4+6/3-2"))   # -5
print(evaluate_expression("-4+2"))              # -2
print(evaluate_expression("3+5*2-8/4"))        # 11
print(evaluate_expression("10/3"))             # 3
print(evaluate_expression("14-3/2"))           # 13