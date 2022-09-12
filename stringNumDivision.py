n=int(input("enter no."))
s=''
i=0
while(i<n):
    if i==n-1:
        p='1/'+str(i+1)
    else:
        p='1/'+str(i+1)+' + '
    s+=p
    i+=1
print(s)