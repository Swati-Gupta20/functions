# def big():
#     unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
#     unorder_list.sort()
#     print(unorder_list)
# big()






def big():
    unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
    l=[]
    min=1000
    i=0
    while(i<len(unorder_list)):
        j=0
        while(j<len(unorder_list)):
            if unorder_list[i]<unorder_list[j]:
                min=unorder_list[j]
            j+=1
        if min not in l:
            l.append(min)
        i+=1
    print(l)
big()



    
