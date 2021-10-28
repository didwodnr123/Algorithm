t = int(input())
lst = sorted(list(map(int, input().split())))
answer, tmp = 0, 0

for i in lst:
    tmp += i
    answer += tmp  

print(answer)
