lst = [1,2,3,4,5,6]
size = len(lst)
half = int(size/2)

if int(size%2)==0:
    paper1 = lst[0:half]

    paper2 = lst[half:size]
    result = [paper1,paper2]
    print(result)
elif int(size%2)==1:
    paper1 = lst[0:half+1]

    paper2 = lst[half+1:size]
    result = [paper1, paper2]
    print(result)
elif size == 0:
    print([], [])
else: print(lst, [])






