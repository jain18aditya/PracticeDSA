dict={"a":10, "c":15, "b":13}

dict = sorted(dict.items(), key= lambda x: x[0])

print(dict)
