def listlen():
    l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    size=len(l)
    max=0
    min=1000
    i=0
    while(i<size):
        j=0
        while(j<size):
            if len(l[i])>max:
                b=l[i]
                max=len(b)
            elif len(l[i])<min:
                a=l[i]
                min=len(a)
            j+=1
        i+=1
    print(max,",",b)
    print(min,",",a)
listlen()