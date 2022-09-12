def unique_L():
    l=[1,2,3,3,3,3,4,5]
    l2=[]
    i=0
    while(i<len(l)):
        if l[i] not in l2:
            l2.append(l[i])
        i+=1
    print(l2)
unique_L()