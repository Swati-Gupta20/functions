def diff(*num):
    l=list(num)
    y=0
    n=0
    i=0
    while(i<len(l)-2):
        if l[i]-l[i+1]==l[i+1]-l[i+2]:
            y+=1
        else:
            n+=1
        i+=1
    if n==0:
        print("true")
    else:
        print("false")

diff(2,3,4,5,6,7,8,10)
    