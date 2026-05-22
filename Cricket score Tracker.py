Score=[]
print("Welcome to cricket score tracker")

while True:
    print("---ScoreCard---")
    print("Add Player Score")
    print("Total Team Runs")
    print("Exit")

    choice= int(input("Enter your choice"))
    if choice==1:
        Name=input("Enter player name")
        Runs=int(input("Enter runs"))
        Balls=int(input("Enter balls"))
        Team= input("Enter his team")

        score={
            "Name": Name,
            "Runs": Runs,
            "Balls": Balls,
            "Team": Team
        }

        Score.append(score)
        print("Added succesfully")

    elif choice==2:
        if(len(Score)==0):
            print("Please add details")
        else:
            print("Details added sucessfully")

            count=1
            for eachkey in Score:
                print(f"Score_card{count}->{eachkey["Name"]},{eachkey["Runs"]},{eachkey["Balls"]},{eachkey["Team"]}")
                count=count+1
    elif choice==3:
        total=0
        for eachkey in Score:
            total= total + eachkey["Runs"]

        print("\nTotal_Runs",total)

    elif choice==4:
        print("Thanks for using it")
        break
    else:
        print("Please Entered Right details")

        




            


        




            

        












