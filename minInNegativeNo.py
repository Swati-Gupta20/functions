def small():
    min=0
    i=0
    while(i<5):
        n=int(input("enter no."))
        if n<min:
            min=n
        i+=1
    print(min)
small()