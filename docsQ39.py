def larlow():
    l=[4,6,2,1,9,63,-134,566]
    max=0
    min=1000
    i=0
    while(i<len(l)):
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
        i+=1
    print(min)
    print(max)
larlow()
    