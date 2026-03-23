
def convert_to_base(n, base):
    result = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n==0:
        return 0

    while n>0:
        reminder = n % base
        result = digits[reminder] + result
        n //= base
    return result

print(convert_to_base(85, 43))
