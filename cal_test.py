list_a = [960, 380, 180, 200, 1080, 460, 650, 410]
for i in range(7):
    index = i
    for j in range(i+1, 8):
        if list_a[index] < list_a[j]:
            index = j
    list_a[i], list_a[index] = list_a[index], list_a[i]

print(list_a)