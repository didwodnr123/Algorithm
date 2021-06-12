N, K = map(int, input().split())
lst = []
answer = 0
for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)
for n in lst:
    if K//n > 0:
        answer += K//n
        K -= (n*(K//n))
        if K <= 0:
            break

print(answer)