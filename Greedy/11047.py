# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

N, K = map(int, input().split())
for i in range(N):
    x = input()
    
coin = 0

a = K//50000
b = K%50000
c = b//10000
d = b%10000
e = d//5000
f = d%5000
g = f//1000
h = f%1000
i = h//500
j = h%500
k = j//100
l = j%100
m = l//50
n = l%50
o = n//10
p = n%10
q = p//5
r = p%5
s = r//1

print(a+c+e+g+i+k+m+o+q+s)