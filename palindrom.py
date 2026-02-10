from turtledemo.penrose import start

s="aditya"

def palindrom(s):
    start = 0
    end = len(s)-1

    while start < end:
        if (s[start] != s[end]):
            return False
        start += 1
        end -= 1
    return True

print(palindrom(s))
print(palindrom("adida"))
print(palindrom("adittida"))

def palindrom_list(s):
    return s[0:] == s[::-1]

print(palindrom_list("aditya"))
print(palindrom_list("adida"))

