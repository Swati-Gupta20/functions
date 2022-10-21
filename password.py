def Authentication(pw):
    if len(pw)<6:
        return 'length must be 6 digits'
    elif len(pw)>15:
        return 'length must be less than 15'
    elif pw[0].isdigit():
        return 'do not start with a digit'
    else:
        up=0
        lo=0
        sc=0
        di=0
        ot=0
        spe='@#$%&?!'
        otr='/." "'
        i=0
        while i<len(pw):
            if pw[i].isupper():
                up+=1
            elif pw[i].islower():
                lo+=1
            elif pw[i].isdigit():
                di+=1
            elif pw[i] in spe:
                sc+=1
            elif pw[i] in otr:
                return "invalid password\ndo not use '/' ,'.' & space"
                break
            i+=1
        if ot>0:
            print("")
        elif up>1 and lo>1 and sc>1 and di>1:
            return 'valid password'
        else:
            return 'invalid password'
result=Authentication(input('enter password:-'))

print(result)



 



 
