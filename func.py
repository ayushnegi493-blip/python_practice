# Functons basic 
def sumFun():
    a=4
    b=8
    sum= a+b
    print(sum)

sumFun()
sumFun()
sumFun() 

def welcome_message():
    print("Welcome to python programming")
welcome_message()
welcome_message()
welcome_message()

def inspire():
    print("Never give up ayush")

inspire()
inspire()
inspire()

def good_morning():
    print("Good morning ayush")
good_morning()
good_morning()
    
# Functions calling with arguments

def avg(a,b):
    avgvalue=(a+b)/2
    print(avgvalue)

avg(5,10)
avg(7,10)
avg(80,98)
avg(2,4)

# wrie a function show age(name,age) that "saumya sing is 21 years old"
def show_age(name,age):
    print(f"{name} is {age} years old")

show_age("saumya",21)
show_age("sapna",25)

# create a functon add numbers(a,b) that prints both the sum and difference
def add_numbers(a,b):
    value= (a+b)
    
    print(value)
add_numbers(66,22)
add_numbers(89,-10)

def fav_food(food):
    print(f"saumya loves {food}")

fav_food("gulabjamun")

#  return statement

def multi(a=10,b=10):
    return a*b
result=multi(5,10)
print(result)

def square (num=10):
    return num*num

result= square(20)
print(result)


def func(userInput):
    vowels="aeiou"
    userInput=userInput.lower()

    countVowel=0
    countConsonents=0

    for i in userInput:
        if(i.isalpha()):
            if(i in vowels):
                countVowel= countVowel+1
            else:
                countConsonents= countConsonents+1

    return countVowel,countConsonents

vowels,consonents= func("Ayush Negi")
print(vowels,consonents)


# Write a function that takes a string and returns the count of vowels and cononants separately

def vowConso(text):
    vowels="aeiou"
    vowels_count=0
    consonents_count=0

    text=text.lower()
    for ch in text:
        if(ch.isalpha()):
            if ch in vowels:
                vowels_count= vowels_count+1
            else:
                consonents_count=consonents_count+1

    print("vowels",vowels_count)  
    print("consonents",consonents_count)

vowConso("ayuSH")
           
           
# Write a function that takes a string and returns the count of vowels and cononants separately

def vowConso(text):
    vowels="aeiou"
    vowels_count=0
    consonents_count=0

    text=text.lower()
    for ch in text:
        if(ch.isalpha()):
            if ch in vowels :
                vowels_count=vowels_count+1
            else:
                consonents_count=consonents_count+1

    print("Vowels",vowels_count)
    print("Consonant",consonents_count)

vowConso("ayush")

# 1. Count Digits and Alphabets

# Take input from user and count:

# total alphabets
# total digits

def digalpha(text):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alpha_count=0
    digit_count=0

    
    text=text.lower()

    for ch in text:
        if(ch.isalpha()):
            if ch in alphabet:
                alpha_count=alpha_count+1
        elif(ch.isdigit()):
            digit_count=digit_count+1

    print("Alphabets",alpha_count)
    print("Digits",digit_count)

digalpha("ayush@454")

# 9. Find Frequency of Character

# Example:

# Input: banana
# Character: a

# Output: 3

def frequency(text):
    alphabet="x"
    alphabet_count=0
    another_alphabet_count=0

    text=text.lower()

    for ch in text:
        if (ch.isalpha):
            if ch in alphabet:
                alphabet_count=alphabet_count+1
            else:
                another_alphabet_count=another_alphabet_count+1

    print("repeated element",alphabet_count)
    return alphabet_count


    

result=frequency("banana")
print(result)

 
#  2. Add Two Numbers

# Write a function that takes 2 numbers and returns their sum.

# Example:

# add(5, 3)
# # Output: 8

def add(a,b):
    
    sum=a+b
    return sum
result= add(4,4)
result=add(8,3)
print(result)

def convert_to_upper(word):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_count=0
    

    word=word.upper()
    for ch in word:
        if (ch.isalpha()):
            if ch in alphabet:
                alphabet_count=alphabet_count+1

    print("Uppercase string",word)
    print("total alphabet", alphabet_count)
convert_to_upper("ayush")

def full_name(fname,lname):
    print(f"her full name is {fname} {lname}")
    return fname,lname

result=full_name("sapna","panwar")
print(result)




 



           








            
            




    


