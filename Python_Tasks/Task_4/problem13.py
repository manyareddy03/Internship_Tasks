# Problem 13: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

m=int(input())
a=map(int,input().split())
n=int(input())
b=map(int,input().split())
c = set(a)
d = set(b)

e=c.union(d)
f=d.intersection(c)
res=(e)-(f)
for i in sorted(res):
    print(i)
    
