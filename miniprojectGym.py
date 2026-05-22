# GYM Membership Tracker

Member=[]
print("Welcome to our GYM Memberbership")
while True:
    print("---Menu---")
    print("Add Member")
    print("View Member")
    print("Total Fee")
    print("Exit")

    choice=int(input("Enter your choice"))
    if (choice==1):
        Name=input("Enter member's name")
        Age= input("Enter age")
        Weight= float(input("Enter weight in KG"))
        Fee= int(input("Enter monthly fee"))

        member={
            "Name": Name,
            "Age" : Age,
            "Weight": Weight,
            "Fee": Fee
        }
        Member.append(member)
        print("Member added sucessfully")

    elif(choice==2):
        if(len(Member)==0):
            print("Please add some members")
        else:
            print("Already added")
            count=1
            for i in Member:
                print(f"{count}-> {i["Name"]},{i["Age"]},{i["Weight"]},{i["Fee"]}")
                count= count +1


    elif(choice==3):
        total= 0
        for i in Member:
            total= total + i["Fee"]
        print("Total fee Collected", total)

    elif(choice==4): 
        print("Thanks to join our Membership")
        break
    else:
        print("Invalid")
        
