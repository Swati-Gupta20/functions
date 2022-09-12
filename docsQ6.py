def evenNo():
    l= [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2=[]
    i=0
    while(i<len(l)):
        if l[i]%2==0:
            l2.append(l[i])
        i+=1
    print(l2)
evenNo()