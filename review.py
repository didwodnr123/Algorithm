N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key = lambda x: x[0])
times.sort(key = lambda x: x[1])

last = 0
answer = 0
for s, e in times:
    if last <= s:
        answer += 1
        last = e
        

print(answer)