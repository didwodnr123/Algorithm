T = int(input())

for _ in range(T):
    lst = list(input())
    answer = []
    count = 0

    for i in range(len(lst)):
        if lst[i] == 'O':
            count += 1
        elif lst[i] == 'X':
            count = 0

        answer.append(count)

    print(sum(answer))
