def solution(citations):
    citations.sort()
    num = len(citations)
    while True :
        for i, value in enumerate(citations):
            if value >= num and len(citations[i:]) >= num :
                return num
        else :
            num -= 1
            continue
        

print(solution([3,0,1,5,6]))