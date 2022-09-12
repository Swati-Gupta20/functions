# def small():
#     list = [8, 6, 4, 8, 4, 50, 2, 7]
#     print(min(list))
# small()

# print(min(max(False,-3,-4), 2,7))



def small():
    list = [8, 6, 4, 8, 4, 50, 2, 7]
    min=1000
    i=0
    while(i<len(list)):
        if list[i]<min:
            min=list[i]
        i+=1
    print(min)
small()
