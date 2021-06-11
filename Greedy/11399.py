N = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
tmp = []
for i in lst:
    tmp.append(i)
    answer += sum(tmp)

print(answer)