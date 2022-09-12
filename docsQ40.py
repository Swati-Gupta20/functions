def square():
    num=input("enter no.")
    i=0
    while(i<len(num)):
        n=int(num[i])**2
        print(n,end="")
        i+=1
square()
