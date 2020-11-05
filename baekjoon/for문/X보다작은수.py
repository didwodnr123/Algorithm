import sys

N, X = map(int, sys.stdin.readline().split())

A = map(int, sys.stdin.readline().split())
answer = []
for a in A:
    if a < X:
        print(a, end=" ")