name=input("Hello frind how are you,Enter your name ")

print("Namaskar dost,how can I help you")
print("You can ask me basic Questions, type 'bye' to exit")

responses= {
    "hello": "Hi.. there",
    "how are you": " I am fine and you?",
    "sad": "Don't worry everything will be Okay",
    "who are you":"I am your AI assistant chatbot",
    "what is your name": "My name is Golu", 
}

def greetUser( userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to do this"

while True:
    UserInput= input("Please ask your question")

    reply= greetUser(UserInput)

    print("Golu Response:", reply)

    if 'bye' in UserInput.lower():
        break


