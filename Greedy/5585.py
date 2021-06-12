n = int(input())
m = 1000 - n
lst = [500, 100, 50, 10, 5, 1]
answer = 0

for l in lst:
    if m == 0: break
    elif m//l > 0:
        answer += m//l
        m %= l

print(answer)