# questions=["Who is the prime minister of India?","What is the color of mango?","Which is the largest state of India?","What is the capital of India?"]


# options=[["Narendra Modi","Amit Shah","Rahul Gandhi","Pranab Mukherjee"],["Pink","Maroon","White","Yellow"],["Haryana","Assam","Rajasthan","Telangana"],[" New Delhi","Ahemdabad","Chandigarh","Kolkata"]]

# solutions=[1,4,3,1]
# lifeline=[["Narendra Modi","Pranab Mukherjee"],["Maroon","Yellow"],["Assam","Rajasthan"],[" New Delhi","Kolkata"]]
# lifesol=[1,2,2,1]
# count=0
# def hint(i):
#         global count
#         if count==0:
#             j=0
#             while(j<len(lifeline[i])):
#                     print(j+1,lifeline[i][j])
#                     j+=1    
#             ans=int(input("enter answer:-"))
#             count+=1
#             if ans==lifesol[i]:
#                 return True
#             else:
#                 return False
#         else:
#             print('lifeline is used')
#         # count+=1
# def sol(i):
#         j=0
#         while(j<len(options)):
#                 print(j+1,options[i][j])
#                 j+=1
#         ans=int(input("enter answer:-"))
#         if ans==solutions[i]:
#                 return True
#         elif ans==5050:
#                 return hint(i)
# def complete():
#     i=0
#     while(i<len(questions)):
#         print("Q",i+1,questions[i])
#         a=sol(i)
#         if a==True:
#             print("your answer is true")
#         else:
#             print("wrong ")
#             break
#         i+=1
# complete()


questions=["Who is the prime minister of India?","What is the color of mango?","Which is the largest state of India?","What is the capital of India?"]
options=[["Narendra Modi","Amit Shah","Rahul Gandhi","Pranab Mukherjee"],["Pink","Maroon","White","Yellow"],["Haryana","Assam","Rajasthan","Telangana"],[" New Delhi","Ahemdabad","Chandigarh","Kolkata"]]
solutions=[1,4,3,1]
lifeline=[["Narendra Modi","Pranab Mukherjee"],["Maroon","Yellow"],["Assam","Rajasthan"],[" New Delhi","Kolkata"]]
lifesol=[1,2,2,1]
count=0
def hint(i):
        global count
        if count==0:
                j=0
                while(j<len(lifeline[i])):
                        print(j+1,lifeline[i][j])
                        j+=1    
                ans=int(input("enter answer:-"))
                count+=1
                if ans==lifesol[i]:
                        return True
                else:
                        return False
        else:
                print('lifeline is used')
                ans=int(input("enter answer:-"))
                if ans==solutions[i]:
                        return True
                else:
                        return False
def sol(i):
        j=0
        while(j<len(options)):
                print(j+1,options[i][j])
                j+=1
        ans=int(input("enter answer:-"))
        if ans==solutions[i]:
                return True
        elif ans==5050:
                return hint(i)
def complete():
    i=0
    while(i<len(questions)):
        print("Q",i+1,questions[i])
        a=sol(i)
        if a==True:
                print("your answer is true")
        else:
                print("wrong ")
                break
        i+=1
complete()