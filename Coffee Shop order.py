print("Welcome to our Coffee Shop")
size= input( "what coffee size do you want? S M L")
extra_sugar= input("if you want extra sugar type Y else N")
whipped_cream= input("if you want cream type Y else N")
bill= 0

if size== "S":
    bill= 80
elif size== "M":
    bill= 120
elif size== "L":
    bill= 160
else:
    print("you enter wrong order")

if extra_sugar=="Y":
     bill+= 10
if whipped_cream== "Y":
            bill+= 20
print(f"your final amount is {bill} $")              

