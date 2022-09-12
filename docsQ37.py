def sheepPresent():
    l=[True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]
    c=0
    i=0
    while(i<len(l)):
        if l[i]==True:
            c+=1
        i+=1
    print(c,'sheeps are present')
sheepPresent()