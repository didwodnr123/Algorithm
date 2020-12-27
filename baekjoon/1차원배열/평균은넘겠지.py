from sys import stdin

T = int(stdin.readline())

for tc in range(T):
    answer = []
    lst = list(map(int, stdin.readline().split()))
    avg = sum(lst[1:len(lst)+1])/lst[0]
    for i in range(1, len(lst)):
        if lst[i] > avg:
            answer.append(lst[i])

    print('%.3f' % (len(answer)/lst[0]*100) + '%')
