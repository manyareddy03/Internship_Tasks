# Problem 6: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(arr):
    total=sum(set(arr))
    s=len(set(arr))
    average=total/s
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
