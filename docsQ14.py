def primeNo():
    num=int(input("enter a number:-"))
    k=0
    if num==1  or num==0:
        print(num,"is not a prime no.")
    else:
        i=2
        while(i<num):
            if num%i==0:
               k=k+1
            i=i+1
        if k==0:
           print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
primeNo()