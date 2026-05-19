expenses= [] #list of expenses in form of dictonary
print("Welcome to expense tracker")

while True:
    print("---Menu---")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. Total spending")
    print("4. Exit")

    choice = int(input("Enter your choice"))

    if (choice ==1):
        date=input("Enter the date")
        category=input("Enter category(food,travel,books etc..)")
        description=input(" Enter details ")
        amount=float(input("Enter the Amount"))

        expense={
            "date": date,
            "category":category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expenses added succesfully")
    elif(choice ==2):
        if(len(expenses)==0):
            print("no expenses added")
        else:
            print("This is your expense-----")

            count =1
            for eachExpense in expenses:
             print(f" Expenses No {count}-> {eachExpense['date']},{eachExpense['category']},{eachExpense['description']},{eachExpense['amount']}")
             count=count +1
    elif(choice==3):
        total=0
        for eachExpense in expenses:
            total= total+ eachExpense["amount"]
        print("\n Total Expense=",total)

    elif(choice==4):
        print("thanks for using it")
        break
    else:
        print("Invalid choice! Try Again")
        


    
    


