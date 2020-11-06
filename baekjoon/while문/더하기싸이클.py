def get_next_number(n):
    p = n // 10  # 앞자리
    q = n % 10  # 뒷자리
    return q*10 + (p+q)%10


n = int(input())
m = n
cycle = 0
while cycle == 0 or n != m:
    m = get_next_number(m)
    cycle += 1

print(cycle)
