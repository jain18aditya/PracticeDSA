# =========================
# PROBLEM 2
# =========================
# Minimum Operations to Reduce N to 0
#
# Given integer n:
# - If n is even → divide by 2
# - If n is odd → either +1 or -1
#
# Return minimum operations to make n = 0


# Optimal (Greedy / Bit Manipulation)
def getMinOperations(n):
    ops = 0

    while n > 0:
        if n & 1 == 0:
        # if n % 2 == 0:
            #n >>= 1
            n //= 2
        else:
            if n == 1 or (n & 3) == 1:
            # if n == 1 or n % 4 == 1:
                n -= 1
            else:
                n += 1

            ops += 1

    return ops

# =========================
# EXAMPLES
# =========================
if __name__ == "__main__":
    print(getMinOperations(5))  # 2
