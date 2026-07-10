list = [1, 3, 8, 7, 5, 2, 4, 10, 6, 9]
for i in range(len(list) - 1):
    for j in range(len(list) - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)