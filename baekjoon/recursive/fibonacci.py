def fibonacci(n):
    if n >= 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0

N = int(input())
print(fibonacci(N))