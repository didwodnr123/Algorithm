n = int(input())
times = []

for i in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

times = sorted(times, key=lambda x: x[0])
times = sorted(times, key=lambda x: x[1])

last = 0
answer = []

for s, e in times:
    if s >= last:
        answer.append([s,e])
        last = e

print(answer)