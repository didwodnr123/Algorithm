def factorial_recursive(n):
    if n > 1:
        return n * factorial_recursive(n-1)
    else:
        return 1

N = int(input())
print(factorial_recursive(N))