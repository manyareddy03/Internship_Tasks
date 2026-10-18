# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input()
message = "SOS"
count = 0

for i in range(len(s)):
    if s[i] != message[i % 3]:
        count += 1

print(count)
