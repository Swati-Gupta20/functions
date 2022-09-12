def speedLimit(speed):
    s1=speed
    if s1<=70:
        print("ok")
    else:
        p=0
        # i=70
        s=71
        while s<=s1:
            p+=1
            s+=5
        if p<12:
            print(p)
        else:
            print("licence suspended")
speedLimit(135)