# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        result = str(first)

        while len(result) < len(s):
            current += 1
            result += str(current)

        if result == s:
            print("YES", first)
            return

    print("NO")

q = int(input())

for _ in range(q):
    s = input().strip()
    separateNumbers(s)
