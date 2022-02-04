n = int(input())
lst = []
for _ in range(n):
    name, score = input().split()
    lst.append((name, int(score)))

lst.sort(key=lambda x: x[1])
for name, score in lst:
    print(name, end=' ')
