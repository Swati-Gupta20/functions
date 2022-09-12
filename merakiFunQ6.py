# def Calculator(num_x,num_y,operator):
#     if operator=="add":
#        c=num_x+num_y
#     elif operator=="subtract":
#         c=num_x-num_y
#     elif operator=="multiply":
#         c=num_x*num_y
#     elif operator=="divide":
#         c=num_x/num_y
#     return c
# add_result=Calculator(23,10,'add')
# print(add_result)
# subtract_result=Calculator(23,10,'subtract')
# print(subtract_result)
# multiply_result=Calculator(23,10,'multiply')
# print(multiply_result)
# divide_result=Calculator(23,10,'divide')
# print(divide_result)

o=input()
def add(n,y):
    s=n+y
    return s
def sub(n,y):
    s=n-y
    return s
def main():
    if o =='add':
       return add(14,7)
    elif o =='sub':
        return sub(14,7)

print(main())





    



