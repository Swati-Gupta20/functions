def generateRange(min, max, step):
    l=[]
    i=min
    while(i<=max):
        l.append(i)
        i+=step
    print(l)
generateRange(1,10,3)