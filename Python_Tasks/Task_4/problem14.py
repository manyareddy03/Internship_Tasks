# Problem 14: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem
n=int(input())
num=set()
for _ in range(n):
    num.add(input())
print(len(num))
