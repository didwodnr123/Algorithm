t = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
answer = 0

for _ in range(t):
    a = min(lst1)
    b = max(lst2)
    lst1.remove(a)
    lst2.remove(b)
    
    answer += a*b
    
print(answer)
