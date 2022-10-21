def evenOdd(num):
    sum=0
    copy=str(num)
    if len(str(num))==1:
        return num
    else:
        i=0
        while(i<len(copy)):
            n=num%10
            sum+=n
            num//=10
            i+=1
        if len(str(sum))==1:
            if sum%2==0:             
                return sum,'is even'
            else:
                return sum,'is odd'
        else:
            return evenOdd(sum)
result=evenOdd(int(input("enter no.")))
print(result)