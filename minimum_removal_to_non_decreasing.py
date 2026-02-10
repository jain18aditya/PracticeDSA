def solution(arr):
    if not arr:
        return 0

    c1 = c2 = c3 = 0

    for x in arr:
        if x == 1:
            c1 += 1
        elif x == 2:
            c2 = max(c1, c2) + 1
        elif x == 3:
            c3 = max(c2, c3) + 1

    return len(arr) - max(c1, c2, c3)


# Robust input parsing
try:
    # line = input().strip()
    line = "[2, 1, 3, 2, 1]"
    line = line.strip()[1:-1]
    if not line:
        print(0)
    else:
        arr = [int(x.strip()) for x in line.split(',') if x.strip()]
        print(arr)
        print(solution(arr))
except Exception:
    print("Exception received")
    print(0)
