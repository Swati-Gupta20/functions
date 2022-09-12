from re import I


def addMultiples(limit):
    sum=0
    i=1
    while(i<=limit):
        if i%3==0 or i%5==0:
            sum+=i
            # print(i)        
        i+=1
    print(sum)
addMultiples(20)