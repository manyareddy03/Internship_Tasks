# Problem 12: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

s1 = input().strip()
s2 = input().strip()

c1 = Counter(s1)
c2 = Counter(s2)

print(sum((c1 - c2).values()) + sum((c2 - c1).values()))
