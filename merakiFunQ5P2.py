def check_numbers_list(l1,l2):
    i=0
    while i<len(l1):
        if l1[i]%2==0 and l2[i]%2==0:
            print("index",i,':',"both integers are even")
        else:
            print("index",i,':',"both integers are not even")
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
