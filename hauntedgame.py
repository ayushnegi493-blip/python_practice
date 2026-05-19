# print("Welcome to the haunted house game")
# choose1=input('Do you want to enter the house type "yes" or "no"')
# if choose1== "yes":
#      choose2= input('Where do you want to go."upstairs" or "downstairs"')
# if choose2== "upstairs":
#     print("YOOOO! HUUU! You found the Gold. You win! ")
# else:
#     print("You attacked by Ghost. Better luck next time")

#   else:
# print("you stayed outside. Game over")

print("Welcome to the haunted house game")

choose1 = input('Do you want to enter the house? type "yes" or "no": ').lower()

if choose1 == "yes":
    choose2 = input('Where do you want to go? "upstairs" or "downstairs": ').lower()

    if choose2 == "upstairs":
        print("YOOOO! HUUU! You found the Gold. You win! 🏆")
    else:
        print("You were attacked by a Ghost. Better luck next time 👻")

else:
    print("You stayed outside. Game over.")
