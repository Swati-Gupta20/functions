def BMI(weight,height):
    hMtr=(height/100)**2
    bmi=weight/hMtr
    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25.0:
        print("Normal")
    elif bmi <= 30.0:
        print("Overweight")
    elif bmi > 30:
        print("Obese")
BMI(50,158)









