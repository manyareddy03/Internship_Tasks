# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weights = set()
previous = ""
current_weight = 0

for char in s:
    value = ord(char) - ord('a') + 1

    if char == previous:
        current_weight += value
    else:
        current_weight = value

    weights.add(current_weight)
    previous = char

for query in queries:
    print("Yes" if query in weights else "No")
