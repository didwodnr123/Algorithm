formula = input().split('-')

answer = 0
cnt = 0

for f in formula:
    if cnt == 0:
        answer += sum(map(int, f.split('+')))
        cnt = 1
    else:
        answer -= sum(map(int, f.split('+')))

        
print(answer)
