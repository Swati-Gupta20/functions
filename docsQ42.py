def sumOfEle():
    l=['12','34','44','62']
    l2=[]
    i=0
    while(i<len(l)):
        j=0
        sum=0
        while(j<len(l[i])):
            sum+=int(l[i][j])
            j+=1
        l2.append(sum)
        i+=1
    print(l2)
sumOfEle()