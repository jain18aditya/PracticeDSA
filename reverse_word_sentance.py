"""
Problem: Reverse Characters of Each Word in a Sentence

Given a sentence (string) consisting of multiple words separated by spaces,
reverse the characters of each word while keeping the word order unchanged.

Return the modified sentence.

Requirements:
- Do NOT change the order of words.
- Reverse only the characters inside each word.
- Preserve spaces between words.
- Handle punctuation as part of the word.
- Handle empty string and single-word input.

Example:
Input:  "Hello World!"
Output: "olleH !dlroW"

Explanation:
- "Hello" → "olleH"
- "World!" → "!dlroW"
- Word order remains the same.

Approach 1:
- Split the sentence into words.
- Reverse each word using slicing.
- Join the reversed words back with spaces.

Approach 2:
- Modify the list of words in-place and rebuild the string.

Approach 3:
- Use generator expression for a concise one-line solution.
"""


def reverse_word(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)

def reverse_word_inplace(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)

def reverse_inline(s):
    return " ".join(word[::-1] for word in s.split())


s= "Hello World!"
print(reverse_word(s))
print(reverse_word_inplace(s))
print(reverse_word_inplace(s))