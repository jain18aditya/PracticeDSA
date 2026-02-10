
def compression_loop(s):
    result = ""
    counter = 0
    for i in range(len(s)-1):
        if s[i] != s[i + 1]:
            result += (s[i] + (str(counter) if counter>1 else ""))
            counter = 0
        counter += 1
    result += (s[-1] + (str(counter) if counter > 1 else ""))

    return result

def compression_inplace(s):
    counter = 0
    writer = 0
    for i in range(len(s)-1):
        if s[i] != s[i + 1]:
            s[writer] = s[i]
            writer += 1
            if counter>1:
                s[writer] = str(counter)
                writer += 1
                counter = 0
        counter += 1
    s[writer] = s[-1]
    if counter > 1:
        writer+=1
        s[writer] = str(counter)
    return "".join(s[:writer+1])

s = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c"]
print(compression_loop(s))
print(compression_inplace(s))

s = "a11bc6"
def decompression(s):
    result = []

    index = 0
    while index < len(s):
        char = s[index]
        index += 1
        multiplier = 0
        while index<len(s) and s[index].isdigit():
            multiplier = multiplier * 10 + int(s[index])
            index += 1
            print(multiplier)

        for i in range(multiplier if multiplier>0 else 1):
            result.append(char)
    return result

print(decompression(s))