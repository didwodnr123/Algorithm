food_times = [3, 1, 2]
k = 5

i = len(food_times)
time = 0
while True:
    time += 1
    if time == k:
        i = i % 3
        break
    i = i % 3
    if food_times[i] == 0:
        i += 1
        continue
    food_times[i] -= 1
    print(food_times)
    if sum(food_times) == 0:
        break
    i += 1

print(i)