s=["aditya", "kanishk", "games", "fly", "play"]

s = sorted(s, key=len)
print(s)

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if len(s[i])>len(s[j]):
            s[i], s[j] = s[j], s[i]

print(s)

