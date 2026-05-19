# Welcome to the tip calculator!
# what was the total bill ? $153.6
# what percentage tip would you like to give ? 10 12 15 15
# how many people to split the bill? 5
# Each person should pay 35.33 $

# print("welcome to the tip calculator")
# bill= float(input("What was the total bill ? $ "))
# tip= int(input("What percentage tip would you like to give 10 12 15 14"))
# people= int(input("How many people to split the bill"))
# Total_bill= bill * (1+tip/100)
# bill_per_person= Total_bill/people 
# Final_amount= round(bill_per_person,2)
# print(f"each person should pay= {Final_amount} $")

# print("Movie split ticket")
# bill= int(input("enter your bill"))
# GST= int(input("enter GST 18"))
# friends= int(input("how many frinds are there"))

# Total_bill= bill* (1+GST/100)
# bill_per_person= float(input(Total_bill/friends))
# Total_amount= round(bill_per_person,2)
# print(f"each friend should pay: {Total_amount} $ ") 

# print("this is electricity bill calculator")
# bill= int(input("enter your bill Rs"))
# gov_subsidy= int(input("enter your discount in percentage"))
# people= int(input("how many people are there"))

# Total_bill= bill * (1 - gov_subsidy/100)
# bill_per_person= float(input(Total_bill/people))
# Total_Amount= round(bill_per_person,2)
# print(f" each person should pay : {Total_Amount} Rs ")

weight= float(input("enter your weight"))
height= float(input("enter your height"))
bmi = weight / (height ** 2)
print(float(bmi))