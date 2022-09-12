def count():
    l=[2, -7, 5, -64, -14]
    cp=0
    cn=0
    i=0
    while(i<len(l)):
        if l[i]>0:
            cp+=1
        elif l[i]<0:
            cn+=1
        i+=1
    print('positive:',cp)
    print('positive:',cn)
count()

