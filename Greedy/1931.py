t = int(input())
lst = []
for _ in range(t):
    a, b = map(int, input().split())
    lst.append((a,b))

lst = sorted(lst, key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])

prev_start, prev_end, cnt = 0, 0, 0
# 시작시간 기준으로 정렬
for i in lst:
    start = i[0]
    end = i[1]
    if start >= prev_end:
        cnt += 1
        prev_end = end
        
print(cnt)
    