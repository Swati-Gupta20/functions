def primeNo(limit):
    i=2
    while(i<=limit):
        j=2
        c=0
        while(j<i):
            if i%j==0:
                c+=1
            j+=1
        if c==0:
            print(i)
        i+=1
primeNo(30)

