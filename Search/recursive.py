# 재귀 함수는 반드시 종료 조건을 명시해야 한다.
# for
def factorial_iterative(n):
    result = 1
    for i in range(1 ,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('Iterative:', factorial_iterative(5))
print('Recursiie:', factorial_recursive(5))