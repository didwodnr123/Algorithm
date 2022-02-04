"""
5
2 3 1 2 2
"""

n = int(input())
array = sorted(list(map(int, input().split())))
result = 0

while array:
    lst = []
    x = array.pop(-1)
    lst.append(x)
    while lst:
        if len(lst) < lst[0]:
            lst.append(array.pop(0))
        elif len(lst) == lst[0]:
            result += 1
            break  

print(result)
