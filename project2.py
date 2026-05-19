# Books=[]
# print("Welcome to our library")
# while True:
#     print("1.Add Book")
#     print("2.View All Books")
#     print("3.Total Books price")
#     print("4. Exit")
#     choice= int(input("Enter your choice"))
#     if(choice==1):
#         name=(input("Enter Book Name"))
#         author=(input("Enter Author Name"))
#         category=(input("Please define Book Category"))
#         price=float(input("Enter price of the Book"))

#         book={
#             "name": name,
#             "author": author,
#             "category": category,
#             "price": price
#         }
#         Books.append(book)
#         print("Book added succesfully")
#     elif(choice==2):
#         if(len(Books)==0):
#             print("Please add some books")
#         else:
#             print("Book has been added")
#             count=1
#             for i in Books:

#                 print(f"No of added Books-> {count}, {i['name']}, {i['author']}, {i['category']}, {i['price']}")
#             count= count +1

#     elif(choice==3):
#         total=0
#         for i in Books:
#               total= total+ i["price"]
#         print("\n Total Books", total)

#     elif(choice ==4):
#         print("Thanks for using Library System") 
#         break
#     else:
#         print("Invalid Choice") 

# Movie collecton Tracker
# Movie=[]
# print("Welcome to movie collection Tracker")
# while True:
#     print("---MENU---")
#     print("Add movie")
#     print("View movie")
#     print("Total movies")
#     print("Exit")

#     choice= int(input("Enter your choice"))
#     if (choice==1):
#         name= input("Enter movie name")
#         Hero_Name=input("Enter hero name")
#         Genre=input("Type what type of movie it is")
#         Rating=input("Enter rating of movie")

#         movie={
#             "name":name,
#             "Hero_Name": Hero_Name,
#             "Genre": Genre,
#             "Rating": Rating
#         }
#         Movie.append(movie)
#         print("Movies added succesfully")
#     elif(choice==2):
#         if(len(Movie)==0):
#             print("Please add some movies")
#         else:
#             print("This is your movies")
#             count=1
#             for i in Movie:
#                 print(f"{count},{i["name"]},i{i['Hero_Name']},{i['Genre']},i{i['Rating']}")
#                 count=count+1

#     elif(choice==3):
        
#         print ("\n Total Movies=",len(Movie))
#         break
#     else:
#         print("Invalid")



# Mobile shop billing management system
# Mobile=[]
# print("Welcome to Mobile shop Billing System")

# while True:

#     print("---Menu---")
#     print("1. Add Mobile")
#     print("2. View Mobile")
#     print("3. Total Bill")
#     print("4. Exit")

#     choice=int(input("Enter your choice"))

#     if(choice==1):

#         Model=input("Type a mobile model name that you want to add")
#         Brand=input("Enter a Brand name that you want to choose")
#         Quantity=int(input("How many mobiles you want"))
#         Price=float(input("Enter amount of mobile"))

#         mobile={
#             "Model": Model,
#             "Brand": Brand,
#             "Quantity": Quantity,
#             "Price": Price
#         }

#         Mobile.append(mobile)

#         print("Phones added sucessfully")

#     elif(choice==2):

#         if(len(Mobile)==0):

#             print("Please add some mobiles")

#         else:

#             print("Already added")

#             count=1

#             for i in Mobile:

#                 print(f"{count}-> {i['Model']},{i['Brand']},{i['Quantity']},{i['Price']}")

#                 count=count+1

#     elif(choice==3):

#         if(len(Mobile)==0):

#             print("Please add some mobiles")

#         else:

#             total=0

#             for i in Mobile:

#                 total = total + i["Quantity"] * i["Price"]

#             print("Total Bill =", total)

#     elif(choice==4):

#         print("Thanks for using it")

#         break

#     else:

#         print("YOU ENTERED INVALID CHOICE")

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

        
            

        
        


                



            

    




   


                
        
            



        
    

        

        

        
    


    




 




    

        








        

    
    
    





