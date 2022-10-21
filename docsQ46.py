def dif():
    l=[45,46,47,48,49,50,51]     
    i=0
    c=0
    b=0
    while i<len(l)-1:
        if l[i+1]-l[i]==1:
            c+=1
        else:
            b+=1
        i+=1
    if b==0:
        return 'true'
    else:
        return 'false'
print(dif())