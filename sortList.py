# accending order:-
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# i=0
# while(i<len(unorder_list)):
#     j=0
#     while(j<len(unorder_list)):
#         if unorder_list[i]<unorder_list[j]:
#             unorder_list[i],unorder_list[j]=unorder_list[j],unorder_list[i]
#         j+=1
#     i+=1
# print(unorder_list)



# decending order:-
unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
i=0
while(i<len(unorder_list)):
    j=0
    while(j<len(unorder_list)):
        if unorder_list[i]>unorder_list[j]:
            unorder_list[i],unorder_list[j]=unorder_list[j],unorder_list[i]
        j+=1
    i+=1
print(unorder_list)