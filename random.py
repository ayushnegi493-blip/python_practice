import random

user_choice= int(input("enter your value. Type 0 for rock, type 1 for paper, type 2 for scissors"))
comp_choice= random.randint(0,2)
print(f" comp choose {comp_choice}")

if user_choice== comp_choice:
    print("draw")
elif user_choice== 0 and comp_choice== 1:
    print("you lose")
elif user_choice==1 and comp_choice==2:
    print("you lose")
elif user_choice==2 and comp_choice==0:
    print("you lose")
elif user_choice==1 and comp_choice== 0:
    print("you win")
elif user_choice== 2 and comp_choice==1:
    print("you win")
elif user_choice==0 and comp_choice==2:
    print("you win")

else:
    print("you are out of the game")



