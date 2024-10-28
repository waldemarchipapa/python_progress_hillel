lst = [1, 0, 2, 0, 3, 0, 4, 0, 5]
i = 0
while i < len(lst):
    if lst[i] == 0:
        del lst[i]
        lst.append(0)
    i += 1
print(lst)
