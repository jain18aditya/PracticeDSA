"""
Problem: String Compression and Decompression

You are given a sequence of characters. Implement algorithms to:

1. Compress the sequence using Run-Length Encoding (RLE).
2. Compress the sequence in-place using constant extra space.
3. Decompress a compressed string back to its original form.

Compression Rules:
- Consecutive repeating characters are replaced by the character followed
  by its count (only if count > 1).
- If a character appears once, only the character is stored (no '1').

Example:
Input (array form):
["a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c"]

Compressed Output:
"ab14c4"

Explanation:
- 'a' appears once → "a"
- 'b' appears 14 times → "b14"
- 'c' appears 4 times → "c4"

------------------------------------------------------------

In-place Compression:
- Modify the input character array directly.
- Use two pointers (reader and writer).
- Do not use extra space beyond O(1).
- Return the compressed string.

------------------------------------------------------------

Decompression:

Given a compressed string where characters may be followed by a number
(possibly multi-digit), reconstruct the original string.

Example:
Input:  "a11bc6"
Output: "aaaaaaaaaaabcccccc"

Explanation:
- 'a11' → 11 times 'a'
- 'b'   → 1 time 'b'
- 'c6'  → 6 times 'c'

Requirements:
- Handle multi-digit counts.
- If no number follows a character, count = 1.
- Preserve original order.

Approach:
- Compression: Count consecutive characters and append char + count.
- In-place: Use writer pointer to overwrite array.
- Decompression: Parse characters and numeric counts using a loop.
"""

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