def numEnd():
    num=int(input("enter no."))
    copy=str(num)
    i=0
    while(i<len(copy)):
        a=(str(num)[-1])
        if a=='0':
            num//=10            
        i+=1
    print(num)
numEnd()



