# def maxi(a,b,c):
#     if a>b and a>c:
#         print(a,"is maximum")
#     elif b>a and b>c:
#         print(b,"is maximum")
#     else:
#         print(c,"is maximum")

# maxi(2,4,8)


def maxi():
    i=0
    max=0
    while(i<3):
        n=int(input("enter no.:"))
        if n>max:
            max=n
        i+=1
    print(max,'is maximum')
maxi()


