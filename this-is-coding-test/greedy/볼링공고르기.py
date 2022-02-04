"""
5 3
1 3 2 3 2
"""
n, m = map(int, input().split())
lst = list(map(int, input().split()))
tmp = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] != lst[j]:
            tmp.append((lst[i], lst[j]))

print(len(tmp))
