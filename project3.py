import datetime
import time
name= input("Swagat hai dost, enter your name:")
presentHour= datetime.datetime.now().hour
if 5 <= presentHour<=11:
    print("Good Morning",name)
elif 11<= presentHour<= 17:
        print("Good Afternoon",name)
    
elif 17<=  presentHour<=20:
        print("Good Evening",name)

else:
        print("Good Night")
        



print("Namaste! Welcome to your Buddy!")
print("You can ask me basic questions,Type 'bye' to exit from the bot")

responses={
    "hello": "Hi,welcome.How can I help you??",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am your AI chatbot",
    "motivate me": " keep going. Every bug of your project makes you a better developer",
    "happy": " Great to hear that",

}

def getResponseBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able not tell that yet. I am in learning mode"

while True:

    userInput=input("Please ask your Question:")
    reply= getResponseBot(userInput)
    print("Bot response:", reply)

    if "bye" in userInput.lower():
        break
    