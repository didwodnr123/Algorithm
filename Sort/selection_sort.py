def selection_sort(lst):
    n = len(lst)
    for i in range(0, n-1):
        minIndex = i
        for j in range(i+1, n):
            if lst[minIndex] > lst[j]:
                minIndex = j
        lst[i], lst[minIndex] = lst[minIndex], lst[i]


lst = [1, 5, 3, 4, 2, 88, 4, 7, -1, 0]
selection_sort(lst)
    
print(lst)
