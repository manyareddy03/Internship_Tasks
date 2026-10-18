# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

def isValid(s):
    counts = Counter(Counter(s).values())

    if len(counts) == 1:
        return "YES"

    if len(counts) != 2:
        return "NO"

    (f1, c1), (f2, c2) = counts.items()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"

    if f1 > f2 and f1 - f2 == 1 and c1 == 1:
        return "YES"

    if f2 > f1 and f2 - f1 == 1 and c2 == 1:
        return "YES"

    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))
