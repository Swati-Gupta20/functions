totalMarks=500



def sumOfMarks():
    marks=[55,64,70,85,65]
    sum=0
    i=0
    while(i<len(marks)):
        sum+=marks[i]
        i+=1
    return sum


def percent():
    a=sumOfMarks()
    per=a/totalMarks*100
    return per

def grade():
    per=percent()
    if per>=90:
        return "grade A"
    elif per>=80 and per<90:
        return "grade B"
    elif per>=70 and per<80:
        return "grade C"
    elif per>=60 and per<70:
        return "grade D"
    else:
        return "grade E"


def result():
    a=print(sumOfMarks())
    b=print(percent())
    c=print(grade())
result()

