import sys

lst = []
for _ in range(9):
    n = int(sys.stdin.readline())
    lst.append(n)

print(max(lst))
print(lst.index(max(lst))+1)

# Best example
# x=[int(input()) for a in range(9)]
# print(max(x),x.index(max(x))+1)
