
def convert_to_base(n, base):
    result = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if n==0:
        return 0

    while n>0:
        reminder = n % base
        result = digits[reminder] + result
        n //= base
    return result

print(convert_to_base(85, 43))


def convert_to_base_modified(n, base):
    if n == 0:
        return "0"

    result = ""

    while n > 0:
        remainder = n % base

        if remainder < 10:
            result = chr(ord('0') + remainder) + result
        elif remainder < 36:
            result = chr(ord('A') + remainder - 10) + result
        else:
            result = chr(ord('a') + remainder - 36) + result

        n //= base

    return result

print(convert_to_base_modified(85, 43))
