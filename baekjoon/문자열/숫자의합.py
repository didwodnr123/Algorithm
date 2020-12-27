T = int(input())
n = int(input())
answer = 0

while True:
    if n == 0:
        break;
    answer += n % 10
    n = n//10

print(answer)