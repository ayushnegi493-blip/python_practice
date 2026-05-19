print("Welcome to Pizza dliveries!")
size= input("What size of Pizza do you want? S, M, L")
pepperoni= input("if you want pepperoni for, type Y if don't type N")
cheese= input("If you want extra cheese type Y if not type N")

bill=0

if size=="S":
    bill+=15
elif size=="M":
   bill+= 20 
elif size=="L":
   bill += 25
else:
   print(input("you enter wrong order"))


   
if pepperoni== "Y":
   if size=="S":
      bill+= 2 
   else:
      bill+= 3
      
if cheese== "Y":
     bill +=1
print(f"you pay {bill} $")
      
   
   
     
