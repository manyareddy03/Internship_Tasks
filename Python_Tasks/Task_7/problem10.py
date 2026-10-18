# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()
count = 1 if s else 0

for char in s:
    if char.isupper():
        count += 1

print(count)
