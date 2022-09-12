def list_change(a,b):
    l=[]
    i=0
    while i<len(a):
        c=a[i]*b[i]
        l.append(c)
        i+=1
    # print(l)
    return l
ml=list_change([2,3,5,4],[3,8,2,7])
print(ml)