s=["aditya", "aditya", "test", "best", "fly", "best", "fly"]


output = list(dict.fromkeys(s))
print(output)

unique = []
seen = set()

for word in s:
    if word not in seen:
        seen.add(word)
        unique.append(word)

print(unique)
