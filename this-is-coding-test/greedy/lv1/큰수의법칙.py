"""
5 8 3
2 4 5 4 6
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0
while m > 0:
    for _ in range(k):
        result += first
        m -= 1
        if m == 0:
            break

    result += second
    m -= 1
    if m == 0:
        break

print(result)
