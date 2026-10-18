# Problem 20: Super Reduced String
# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
stack = []

for char in s:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

result = "".join(stack)
print(result if result else "Empty String")
