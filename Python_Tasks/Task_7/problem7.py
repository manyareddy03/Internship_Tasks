# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    result = []
    
    for i in range(size):
        
        s = alpha[i:size][::-1] + alpha[i+1:size]
        result.append("-".join(s).center(4 * size - 3, '-'))
    
    
    print("\n".join(result[::-1] + result[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
