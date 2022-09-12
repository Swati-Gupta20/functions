def uplow():
    sen='The quick Brow Fox'
    uc=0
    lc=0
    i=0
    while(i<len(sen)):
        if sen[i].isupper():
            uc+=1
        elif sen[i].islower():
            lc+=1
        i+=1
    print('uppercase:',uc)
    print('lowercase:',lc)
uplow()


