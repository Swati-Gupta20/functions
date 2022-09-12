# def back():
#     reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
#     reverse_list.reverse()
#     print(reverse_list)
# back()



def back():
    reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    l=[]
    i=0
    while(i<len(reverse_list)):
        l.append(reverse_list[(i+1)*-1]) 
        i+=1   
    print(l)
back()

