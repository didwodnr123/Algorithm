N = int(input())
lst_n = list(map(int, input().split()))
M = int(input())
lst_m = list(map(int, input().split()))

def binary_search(target, start, end, lst_n):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == lst_n[mid]:
        return 1
    elif target < lst_n[mid]:
        return binary_search(target, start, mid-1, lst_n)
    else:
        return binary_search(target, mid+1, end, lst_n)

lst_n.sort()

for m in lst_m:
    start = 0
    end = len(lst_n)-1
    print(binary_search(m, start, end, lst_n))