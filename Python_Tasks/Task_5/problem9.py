# Problem 9: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=[]
for i in range(n):
    word=input()
    a.append(word)
count={}
for word in a:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(len(count))
print(*count.values())

