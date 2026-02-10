from collections import defaultdict

def group_anagrams(words):
    anagrams_dict = {}
    for word in words:
        key = "".join(sorted(word))
        if key in anagrams_dict:
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]
    return list(anagrams_dict.values())

def group_anagram_defaultdict(words):
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram_defaultdict(arr))
print(group_anagrams(arr))