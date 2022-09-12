questions=["Who is the prime minister of India?","What is the color of mango?","Which is the largest state of India?","What is the capital of India?"]

options=[["Narendra Modi","Amit Shah","Rahul Gandhi","Pranab Mukherjee"],["Pink","Maroon","White","Yellow"],["Haryana","Assam","Rajasthan","Telangana"],[" New Delhi","Ahemdabad","Chandigarh","Kolkata"]]

solutions=['1','4','3','1']
lifeline=[["Narendra Modi","Pranab Mukherjee"],["Maroon","Yellow"],["Assam","Rajasthan"],[" New Delhi","Kolkata"]]
lifesol=['1','2','2','1']
count=0

def hint(i):
    global count
    if count==0:
        count+=1
        j=0
        while(j<len(lifeline[i])):
            print(j+1,lifeline[i][j])
            j+=1
        print("type 'quit' to quit the game")    
        ans=input("enter answer:-")
        if ans==lifesol[i]:
            return True
        elif ans=="quit":
            return 'quit'
    else:
        print("lifeline is used")
        return 'lifeline is used'

    
def sol(i):
    print("type '5050' for lifeline")
    print("type 'quit' to quit the game")
    ans=input("enter answer:-")   
    p=0
    while(p<1):
        if ans==solutions[i]:
            return True
        elif ans=='5050':
            return (hint(i))
        elif ans=='quit':
            return 'quit'
        p+=1      

def complete():
    i=0
    while(i<len(questions)):
        print("Q",i+1,questions[i])
        j=0
        while(j<len(options[i])):
            print(j+1,options[i][j])
            j+=1
        a=sol(i)
        if a==True:
            print("Congrats! correct answer")
        elif a=='lifeline is used':
            a=sol(i)
            if a==True:
                print("Congrats! correct answer")
            else:
                print("wrong answer")
                break
        elif a=='quit':
            print("you quit the game")
            break
        else:
            print("wrong answer")
            break
        i+=1
complete()




    






