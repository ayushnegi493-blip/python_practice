# Gross Salary Calculator

Basic_Salary= int(input("enter basic salary"))
HRA = (20 / 100) * Basic_Salary
DA = (10/100) * Basic_Salary
Gross_Salary= Basic_Salary + HRA + DA

print(Gross_Salary)

# Distance Calci

Distance=int(input("how much distance you cover"))
Time=int(input("How much time you take"))

Speed= Distance/Time
print(Speed)
if Speed <=30:
    print('slow')
elif Speed>30:
    print('Normal')

else:
    print('Fast')

Distance=int(input("How much distance you cover"))
Fuel=float(input("How much fuel you have"))

Milage= Distance/Fuel
print(Milage)
if Milage<=15:
        print("Poor Milage")
elif Milage<=25:
        print("Good Milage")
else:
        print("Excilent")
       

# Emoji converter
Mood= input("enter your mood")
Mood= Mood.replace("Happy","😊")
Mood= Mood.replace("Sad","😢")
Mood= Mood.replace("Normal","😄")
Mood= Mood.replace("Excited","😉")
print(Mood)

# Write a python program that takes a number as input and print

number=int(input("enter a number"))

if number>0:
      print("positive")
elif number==0:
      print("zero")
elif number<0:
      print("negative") 
else:
      print("you entered wrong number")  

    #   list in python
food=["cholt bhature"," gulab jamun","apple","mango"]
print(len(food))
print("third value of list",food[3])

# for append
marks=[99,100,90,95]
marks.append(92)
print(marks)

# sorting
marks=[99,100,90,95]
marks.sort()
print(marks)

# pop
marks=[99,100,90,95]
marks.pop(2)
print(marks)

# remove
marks=[99,100,90,95]
marks.remove(99)
print(marks)

# insert
marks=[99,100,90,95]
marks.insert(1,98)
print(marks)

# take 3 food and store in list, print list and length

Food1= input("enter your favorite food")
Food2= input("Enter your favorite food")
Food3= input("enter your favorite food")

FoodList= [Food1,Food2,Food3]
print(FoodList)

print(len(FoodList))

# TUPLES IN PYTHON

MYtuples=(78,34,35,89)
studenttuple=("ayush","rohan","sapna","lokesh")

print(studenttuple[2])

emptyTuple=()
print(type(emptyTuple))

movie1=input("enter your favorite movie name")
movie2=input("enter your favorite movie name")
movie3=input("enter your favorite movie name")

movie=[movie1,movie2,movie3]
print(movie)

# print highest and minimum

tuple1=int(input("enter number "))
tuple2=int(input("enter number "))
tuple3=int(input("enter number "))
tuple4=int(input("enter number "))
tuple5=int(input("enter number "))
tuple=(tuple1,tuple2,tuple3,tuple4,tuple5)
print(max(tuple))
print(min(tuple))

# Dictionary in python
student={
      "name":"Ayush Negi",
      "city": "Dehradun",
      "age": 26,
      "RollNumber": 7
}
print(student["name"])
print(student["city"])
print(type(student))
print(student)
student["city"]="Meerut"
print(student)
student["faovorite subject"]="Physics"
print(student)

student={
      "name":"Ayush Negi",
      "city": "Dehradun",
      "age": 26,
      "RollNumber": 7
}
print(student["name"])
print(student["city"])
print(type(student))
print(student)
student["city"]="Meerut"
print(student)
student["favorite subject"]="Physics"
print(student)
student.pop("favorite subject")
print(student)

# Create a dictionary named marks to store marks of 3 subjects. 
# add the subjects one by one and print the final dictionary

Marks={
      "Physics": 76,
      "Maths": 79,
      "Operating Systems": 65,

     

}
print(Marks)
Marks["Java"]= 78
Marks["Computer System Architecture"]= 64
Marks["Data Science"]= 56
print(type(Marks))
print(Marks)

# sets

# Loops in python
# print the name 100 times
num=1
while num<=5:
      print("ayush negi")
      num= num+1

print("now we are out of the while loop")

# Q1 write a python program to print numbers from 1 to 10 using a while loop

num=1
while num<=10:
      print(num)
      num=num+1

 # q2 print 10 to 1 using while loop 

num=10
while num>=1:
      print(num)
      num= num-1

# Q3 print all even numbers between 1 to 50 using a while loop

num=1
while num<=50:
      if num%2==0:
            print(num)
      num=num+1

# white a program to print n natural numbers sum

n= int(input("enter your value"))

num=1
while num<=n:
      print(num)
      sum= num*(num+1)/2
      print(sum)

      num= num+1

# printing star pattern

n= 1
while n<=4:
      print("*" * n)
      n=n+1

print("we are out of the while loop")

# Saumya want to print her name 5 tiimes, but each time with a number in front of it. Writ a program using a while loop tha prints

n=1
while n<=5:
      print(n,"Saumya Singh")
      n=n+1

# Write a program to prnt the multiplication table of anu mu;mner using awhile loop 

n=int(input("enter a number"))
num=1
while num<=10:
      print("num*n",num*n)
      
      num=num+1

n=int(input("enter a number"))
num=1
while num<=10:
      print(f"{n} x {num}=  {n*num}")
      
      num=num+1

# FOR loops

food_list=["cake","mango","pizza"]
for i in food_list:
      print(i)

collegesTuple=("ditu","iitd","UPES")
for i in collegesTuple:
      print( "TOP Colleges are", collegesTuple)
 

#  Range 
for i in range(1,8,1):
      print(i)

for i in range(2,20,2):
      print(i)

for i in range(2,21,2):
      print(i)


# Write a program to print numners form m1 to 50 but print Saumya singh insteead of numbers the numbers that are multiplies of 5
for i in range(1,51,1):
      if i%5==0:
            print("Saumya Singh")
      else:
            print(i)


for i in range(1,11,1):
      print(i*i)

# table print 
num=int(input("enter a number"))
for i in range(1,11,1):
      print(f"{num} X {i} =",num*i)

# reverse 100-1 print 
for i in range(100,0,-1):
      print(i)
# PRINT SAUMYASINGH 5 times in upper case 
for i in range(1,6,1):
      print("saumyasingh".upper())

num=1
while num<=5:
      print("saumyasingh".upper())
      num=num+1

      # countires travelled

CountriesTraveled=("Malaysia","Vietnam","Switzerland","Italy","Bhutan")
for i in CountriesTraveled:
      print(i)

for num in range (1,10):
      if num==5:
            break
      print(num)

for num in range (1,10):
      if num==5:
            continue
      print(num)

# print a countdown before something exciting happens( like LAunching happy new year!)
import time
count=int(input("enter the counter num"))
print("countdown starts now:")
for i in range(count,0,-1):
      print(i)
      time.sleep(1)

print("\n Whooo! Happy New year")


# 2. Traffic Signal Simulator

# Print:

# Red → wait 3 sec
# Yellow → wait 2 sec
# Green → GO!

# Hint: use multiple time.sleep()
import time
count=int(input("Enter a number:"))
print("Waiting for single")
for i in range(count,0,-1):
      print(i)
      
      print(" RED 🔴")
      time.sleep(3)
      
      print(" YELLOW 🟡")
      time.sleep(2)
      print( " GREEN 🟢")
      print("lets go")
print("this is Traffic signel🚦")

# 3. Bomb Timer 💣

# User enters seconds.

# # Example:
import time
count= int(input("enter timer in seconds"))
print("Countdown Stars Now! 💀")
for i in range(count,0,-1):
     
      print(i)

      time.sleep(1)
print("BOOOM!💥")

# 10. Mini Game Loading Screen 🎮

# Print:

# Loading.
# Loading..
# Loading...

# with delay.

# Then:

# Game Started!
import time
   
print("loading.")
time.sleep(2)
print("loading..")
time.sleep(2)
print("loading...")
time.sleep(2)
print("Game has started 🎮")


# 4. Morning Alarm

# Print:

# Wake up!
# Brush your teeth
# Get ready for college

# with 2 sec gap between each line.

import time
count=int(input("Press 3 to start Reminder"))
print("Reminder Starts Now")
print("Wake up! ⏰")
time.sleep(2)
print("Brush your Teeth 🪥")
time.sleep(2)
print("Get Ready for College 🏫🏃‍♀️‍➡️")


# Q9. Rocket Launch 🚀

# Print:

# Checking Fuel...
# Checking Engine...
# Launching in:
# 5
# 4
# 3
# 2
# 1
# 🚀 Rocket Launched!

import time
count= int(input("Enter 5 to launch Rocket"))
print("Rocket is Ready to launch")
time.sleep(2)
print("Checking Fuel...")
time.sleep(1)
print("Checking Engine...")
time.sleep(1)
print("Launcing in...")
time.sleep(1)

for i in range(count,0,-1):
      print(i)
      time.sleep(2)

print("Rocked Launched 🚀") 


# Q12. Quiz Timer

# Ask a question and give user only 10 seconds mentally 😭

# Then print:

# Time Over!

import time
count=int(input("Enter how many Questions you want to Practice"))
print("Quick General Knowledge quiz covering a mix of science, history, geography")

if count>=1:
      print("1.Which planet in our solar system is known for having the most extensive and visible ring system ?" \
"\nA)Naptune\nB)Uranus\nC)Saturn\nD)Jupiter")
      ans= input("Enter your answer").strip().upper()
      if ans =="C":
            print("Correct")
      else:
            print("Wrong! C is correct")

      
      time.sleep(3)

if count>=2:
      print("2.What is the capital city of Australia?" \
"\nA)Sydney\nB)Canberra\nC)Brisbane\nD)Melbourn ")
      ans= input("Enter your answer").upper()
      if ans=="B":
            print("Correct")
      else:
            print("Wrong! B is correct")
      time.sleep(3)

if count>=3:
      print("3.Who painted the famous 16th-century portrait known as the Mona Lisa?" \
"\nA)Leonardo Da Vinchi\nB)Pablo Picasso\nC)Michleangelo\nD)Tormus")
      ans= input("Enter your answer").upper()
      if ans=="A":
            print("Correct")
      else:
            print("Wrong! A is correct")
      time.sleep(3)

if count>=4:
      print("4.Which element on the periodic table has the chemical symbol 'O'" \
"\nA)Oganesson\nB)Osmuim\nC)Gold\nD)Oxygen")
      ans= input("Enter your answer").upper()
      if ans=="D":
            print("Correct")
      else:
            print("Wrong! D is correct")
      time.sleep(3)

if count>=5:
      print("5.Which is the largest and deepest ocean on Earth?" \
"\nA)Pacific Ocean\nB)Atlantic Ocean\nC)Arctic Ocean\nD)Indian Ocean")
      ans= input("Enter your answer").upper()
      if ans=="A":
            print("Correct")
      else:
            print("Wrong! A is correct")
      time.sleep(3)
print("-----xxxx------")

print("Time is OVER ⏰")

# you are requird to build a simple personal finance tool. expense management tracker




