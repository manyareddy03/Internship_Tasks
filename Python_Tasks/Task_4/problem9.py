# Problem 9: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    string=''.join(a)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
