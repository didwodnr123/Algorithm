def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range (n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


lst = [1, 5, 3, 4, 2, 88, 4, 7, -1, 0]
bubble_sort(lst)
    
print(lst)
