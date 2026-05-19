print("Welcome to the Water Park")
height = float(input("enter your height in cm"))
bill = 0

if height >= 110:
    print("You can join the water park")
    age = int(input("enter your age"))

    if age < 12:
        bill = 10
        print("you pay 10 $")
    elif age >= 12 and age <= 18:   # fixed age condition
        bill = 15
        print("you pay 15 $")
    else:
        bill = 20
        print("you pay 20 $")

    want_locker = input("if your answer is yes type y and answer is no type n ")
    if want_locker == "y":
        bill += 5

    print(f"you pay total amount of {bill} $")  # print was missing

else:
    print("you can't join")
 