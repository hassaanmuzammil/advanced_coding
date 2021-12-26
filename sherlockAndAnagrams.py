"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
"""

from collections import Counter

def find_all_possible_substrings_sorted(s):
    substrings = [c for c in s]
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            substring = s[i:j]
            if len(substring) > 1 or len(substring) < len(s):
                substrings.append(''.join(sorted(substring)))
    return substrings

def sherlock_and_anagrams(s):
    substrings = find_all_possible_substrings_sorted(s)
    counter = Counter(substrings)
    filtered = {k:v for k,v in counter.items() if v > 1}
    anagrams = sum([sum(range(v) for v in filtered.values())])
    return anagrams

s = "ifailuhkqq"
sherlock_and_anagrams(s)
# returns 3 
