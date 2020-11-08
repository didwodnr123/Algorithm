lst = []
for _ in range(10):
    n = int(input())
    lst.append(n % 42)

lst = set(lst)
print(len(lst))

# Best Example
# b = [int(input())%42 for i in range(10)]
# print(len(set(b)))
