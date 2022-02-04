lst = list(map(int, input()))
result = 1

for num in lst:
    if num == 0 or num == 1:
        result += num
    else:
        result *= num

print(result)
