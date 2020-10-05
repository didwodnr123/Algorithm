def bruteForce(n, m, card):
    answer = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (card[i] + card[j] + card[k]) <= m and m - (card[i] + card[j] + card[k]) < m - answer:
                    answer = card[i] + card[j] + card[k]

    print(answer)


N, M = map(int, input().split())

cards = list(map(int, input().split()))
bruteForce(N, M, cards)
