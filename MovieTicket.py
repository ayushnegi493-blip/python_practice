print(" Welcome to Movie Ticket Counter ")
age= int(input("enter your age"))
popcorn=input("if you want popcorn type Y else N")
bill= 0

if age<12:
    bill= 100 
elif age >12 and age<=60:
    bill= 200
else:
    bill= 150

if popcorn=="Y":
    bill+= 50

    print(f"your final amount is {bill} Rs")




