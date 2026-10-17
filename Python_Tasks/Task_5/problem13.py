# Problem 13: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    scores_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_dict[name] = score
        
    unique_scores = sorted(list(set(scores_dict.values())))
    second_lowest = unique_scores[1]
        
    for name in sorted(scores_dict.keys()):
        if scores_dict[name] == second_lowest:
            print(name)
