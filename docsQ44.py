def lastEle(last):
    copy=last
    l=['a', 1, '2', 5, 'b', 'q']
    i=0
    while(i<copy):
        print(l[-(i+1)])
        i+=1
        # last-=1
lastEle(3)