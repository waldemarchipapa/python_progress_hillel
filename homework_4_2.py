lst = [0, 1, 7, 2, 4, 8]
i = 0
lst_sum = 0
while i < len(lst):
    if i % 2 == 0:
        lst_sum += lst[i]
    i += 1

print(lst_sum * lst[-1])


