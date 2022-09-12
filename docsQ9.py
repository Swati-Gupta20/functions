def  squareList(num1,num2):
    l1=[]
    l2=[]
    i=0
    while(i<5):
        s1=num1**2
        s2=num2**2
        l1.append(s1)
        l2.append(s2)
        num1+=1
        num2-=1
        i+=1
    l2.reverse()
    l=l1,l2
    print(l)
squareList(1,30)

