# Problem 14: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    first = Counter(s[:mid])
    second = Counter(s[mid:])

    return sum((first - second).values())

q = int(input())

for _ in range(q):
    s = input().strip()
    print(anagram(s))
