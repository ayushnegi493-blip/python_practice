Youtube=[]
print("Hey Welcome,how can I help you")
while True:
    print("---MENU---")
    print(" 1.Add video")
    print(" 2.Total Views")
    print(" 3.Most Viewed Video")
    print(" 4.Exit")

    choice=int(input("Enter your choice"))

    if choice==1:
        Video_Title= input("Enter Title of the video")
        Channel_Name= input("Search Channel name")
        Views= int(input("Enter how many views"))
        Likes= int(input("Enter how many likes"))

        youtube={
            "Video_Title": Video_Title,
            "Channel_Name": Channel_Name,
            "Views": Views,
            "Likes": Likes
        }
        Youtube.append(youtube)
        print("Content added sucessfully")

    elif(choice==2):
        if (len(Youtube)==0):
            print("Please add something")
        else:
            print("Already added")

            count=1
            for eachkey in Youtube:
                print(f"details->{count},{eachkey['Video_Title']},{eachkey['Channel_Name']},{eachkey['Views']}",{eachkey['Likes']})
                count= count +1
    elif(choice==3):
        Views=0
        for eachkey in Youtube:
            Views=Views + eachkey["Views"]
        print("Total Views",Views)

    elif(choice==4):
        print("Thanks for using our app")
        break
    else:
        print("Please enter right choice")


           




            


 
# Youtube=[]
# print("Hey Welcome,how can I help you")
# while True:
#     print("---MENU---")
#     print(" 1.Add video")
#     print(" 2.Total Views")
#     print(" 3.Most Viewed Video")
#     print(" 4.Exit")

#     choice=int(input("Enter your choice"))

#     if choice==1:
#         Video_Title= input("Enter Title of the video")
#         Channel_Name= input("Search Channel name")
#         Views= int(input("Enter how many views"))
#         Likes= int(input("Enter how many likes"))

#         youtube={
#             "Video_Title": Video_Title,
#             "Channel_Name": Channel_Name,
#             "Views": Views,
#             "Likes": Likes
#         }
#         Youtube.append(youtube)
#         print("Content added sucessfully")

#     elif(choice==2):
#         Views=0
#         for eachkey in Youtube:
#             Views=Views + eachkey["Views"]

#         print("Total Views",Views)

#     elif(choice==3):
#         if (len(Youtube)==0):
#             print("Please add something")
#         else:
#             print("Already added")

#             count=1
#             for eachkey in Youtube:
#                 print(f"details->{count},{eachkey['Video_Title']},{eachkey['Channel_Name']},{eachkey['Views']},{eachkey['Likes']}")
#                 count= count +1

#     elif(choice==4):
#         print("Thanks for using our app")
#         break

#     else:
#         print("Please enter right choice")
