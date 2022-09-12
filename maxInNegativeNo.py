def big():
    max=-1000
    i=0
    while(i<5):
        n=int(input("enter no."))
        if n>max:
            max=n
        i+=1
    print(max)
big()