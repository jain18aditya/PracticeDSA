#Reverse the order of words in a given sentence (an array of characters). The words given are "Hello World!".

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