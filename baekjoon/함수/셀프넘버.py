def d(n):
    lst = list(str(n))
    result = 0
    for i in lst:
        result += int(i)

    self_nums.append(result + n)


self_nums = []
nums = [x for x in range(1, 10001)]

for n in nums:
    d(n)

a = set(self_nums)
answer = [n for n in nums if n not in a]

for n in answer:
    print(n)


# def selfnumber(num):
#     sum = num
#     while(1):
#         if num == 0 :
#             break
#         sum += num % 10
#         num = num//10
