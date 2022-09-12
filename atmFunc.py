balance=50000
pincode=1234
def deposit():
    print("insert your card")
    amount=int(input("enter amount:-"))
    pin=int(input("enter your pin no."))
    if pin==pincode:
        print("processing")
        print("successfully deposited")
        print("your current balance is",balance+amount)
        return True
    else:
        print("wrong pin no.")
        return False

def withdraw():
    print("insert your card")
    amount=int(input("enter amount:-"))
    pin=int(input("enter your pin no."))
    if pin==pincode:
        if amount>balance:
            print("insufficient balance")
            return False
        else:          
            print("processing")
            print("successfully withdrawl")
            print("your current balance is",balance-amount)
            return True
    else:
        print("wrong pin no.")
        return False

def checkbalance():
    print("insert your card")
    pin=int(input("enter your pin no.:-"))
    if pin==pincode:
        print(balance)
        return True
    else:
        print("wrong pin no.")
        return False


def greet():
    i=0
    while True:
        print("Welcome to State Bank Of India")
        start=input("write 'start' to start the services:-")
        if start=='start':
            print("1 = withdraw")
            print("2 = check_balance")
            print("3 = deposit")
            transaction=input("select any service:-")
            if transaction=='1':
                a=withdraw()
            elif transaction=='2':
                a=checkbalance()
            elif transaction=='3':
                a=deposit()   

            if a==True:
                exit=input("write 'exit' to exit:-")
            elif a==False:
                again=input("write 'tryagain' to try again:-")
                if again=='tryagain':
                    a=greet()
                else:
                    exit=input("write 'exit' to exit:-")
        else:
            print("type correctly")
        i+=1        
greet()





    

