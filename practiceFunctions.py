# def sum(a,b):
#     c=a+b
#     # print(c)
#     return c
# # sum(5,5)
# print(sum(5,5))


# def sum():
#     print(12+13)
# sum()

# def welcome():
#     print("Welcome to function")
# welcome()



# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")

# isEven()


# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Swati")


# def add_numbers(number1, number2):
#     print("I will add two numbers.")
#     print(number1 + number2)
# add_numbers(120, 50)
# num_x = '134'
# name = "Rinki"
# add_numbers(num_x, name)



# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love",flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")



# def greet(*names):
#     for name in names:
#        print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")


# def info(name, age='12'):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")


# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello" , name, "your" , currentMilestone, "concept" , "is clear with the help of",mentorName)


# studentDetails("Swati","functions","Seminao")


# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print("Will i reach here?")
#     return number_sum
# sum6 = add_numbers_more(100, 20)
# print(sum6)



# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print(sum4)
# print(type(sum4))




# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
#     print("Will I be able to print? :-(")

# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# print(fri_menu)



# def distance(kms):
#     if kms < 20:
#         print("close")
#     elif kms < 50:
#        print('median')
#     else:
#         print('far')
# distance(20)



# def f1(a,b):
#     def f2():        
#         c=a+b
#         print(c)
#     f2()
# f1(3,4)



# def f1(a,b):
#     c=a+b
#     return c


# def f2():
#     print(f1(3,6))
# f2()






# a="(){}[]"
# n=input("enter bracket:")
# i=0
# if n[i]=='(' and n[i+1]==')':
#     print("true")
# elif n[i]=='[' and n[i+1]==']':
#     print("true")
# elif n[i]=='{' and n[i+1]=='}':
#     print("true")
# elif n[i]=='[' and n[i+1]==']':
#     print("true")
# else:
#     print("false")





# def pairCount():
#     l=[10,20,20,10,17,40,60]
#     l2=[]
#     i=0
#     while(i<len(l)):
#         count=l.count(l[i])
#         if l[i] not in l2:
#             l2.append(count)
#             l2.append(l[i])
#         i+=1
#     a=l2.count(2)
#     print(a)
# pairCount()



# i=0
# s=0
# count=0
# while(i<len(questions)):
#     print(questions[i])
#     j=0
#     k=0
#     while(j<len(options[i])):
#         print(j+1,".",options[i][j])
#         j+=1
#     ans=int(input("choose your answer:-"))
#     if ans==solutions[s]:
#         print("Congrats this is the right answer.")
#     elif ans==5050:
#         if count!=0:
#             print("5050 lifeline is used")
#             ans=int(input("choose your answer:-"))
#             if ans==solutions[s]:
#                 print("Congrats this is the right answer.")
#             else:
#                 print("wrong answer")
#         else:
#             while(k<len(lifeline[i])):
#                 print(k+1,".",lifeline[i][k])
#                 k+=1
#             count+=1
#             ans=int(input("choose your answer:-"))
#             if ans==lifesol[i]:
#                 print("Congrats this is the right answer.")
#             else:
#                 print("wrong answer")
#                 break
#     else:
#         print("wrong answer")
#         break
#     s+=1
#     i+=1


# names=["swati","ariya","seminao","vilichon","jian","teresa"]
# rooms=[1,2,3]
# i=0
# while i<len(rooms):
#     j=0   
#     while j<len(rooms):
#         print("Room:",rooms[j])
#         print("1.",names[i])
#         print("2.",names[i+1]) 
#         i+=2        
#         j+=1 




# x=lambda a:a*a+a
# print(x(4))

# i=0
# while(i<5):
#     j=0
#     while(j<i+1):
#         print(j+1,end=' ')
#         j+=1
#     i+=2
#     print()
    


# year=int(input("enter year:-"))
# if year%400==0:
#     'leapYear'==True
# elif year%4==0:
#     'leapYear'==True
# elif year%100









