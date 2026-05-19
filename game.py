print("Welcome to the treasure island\nYour mission is to find the treasur")
choose1= input('Where do you want to go? "left" or "right"')
if choose1== "left":
    choose2= input('do you want to "wait" or "swim"')
    if choose2== "wait":
        choose3= input("Which color do you want to choose")
        if choose3== "red":
         print("You caught in fire. Game over")
        elif choose3== "blue":
            print("by by better luck next time")
        elif choose3== "yellow":
                print("you win the Game")
        else:
                print("you enter wrong color. game over")
    else:
        print("you have eaten by sea monster. Game over")
else:
    print("Better luck next time")
    






