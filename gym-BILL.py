print("Heartly Welcome to Premium Gym Membership")
age= int(input("enter your age"))
bill= 0


if age>= 16:
    print("you can join gym")
    Age=int(input("enter your Age"))
    if Age<18:
        bill=15
        print("you pay 15 $")
    elif Age >18 and Age <40:
        bill=25
        print("you pay  25 $")
    else:
        bill= 20
        print("you pay 20 $")

    want_personal_Trainer= input("if you want personal trainer type y if dot't want type n")
    if want_personal_Trainer=="y":
     bill += 10
    print(f"Your total amount is {bill} $")

else:
    print("you can't join gym")
