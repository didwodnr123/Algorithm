import sys

T = int(input())

score = list(map(int, sys.stdin.readline().split()))
max_score = max(score)
result = 0

for i in range(T):
    result += score[i]/max_score * 100

print(result/T)



