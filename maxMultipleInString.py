def multiple():
    num=input('enter no:-')
    if len(num)==0:
        print('invalid string')
    elif len(num)==1:
        print(num)
    else:
        i=0
        sum=0
        while i<len(num)-1:
            mul=int(num[i])*int(num[i+1])
            if mul>sum:
                sum=mul
            i+=1
        print(sum)

multiple()