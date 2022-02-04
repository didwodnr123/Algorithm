"""
5
3 2 1 1 9
"""

n = int(input())
data = sorted(list(map(int, input().split())))
# 1 1 2 3 9
target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)

