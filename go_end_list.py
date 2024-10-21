lst = [12, 3, 4, 10]
if 1 >= len(lst) <= 0:
    print(lst)
else:
    last_elem = lst[-1]
    del lst[-1]
    lst.insert(0, last_elem)
    print(lst)



