a = int(input())
b = int(input())
c = int(input())

abc = list(str(a * b * c))
count = [0]*10
for c in abc:
    if c == '0':
        count[0] += 1
    elif c == '1':
        count[1] += 1
    elif c == '2':
        count[2] += 1
    elif c == '3':
        count[3] += 1
    elif c == '4':
        count[4] += 1
    elif c == '5':
        count[5] += 1
    elif c == '6':
        count[6] += 1
    elif c == '7':
        count[7] += 1
    elif c == '8':
        count[8] += 1
    elif c == '9':
        count[9] += 1

for c in count:
    print(c)

# Best Example
# a = int(input())
# b = int(input())
# c = int(input())
#
# d = list(map(int, (str(a * b * c))))
#
# for i in range(10):
#     print(d.count(i))
