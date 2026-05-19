# print(("ayush negi" +"\n")*10)
# print("line 1")
# print("line 2")
# print("line 3")

# name= "ayush "
# age1= 25
# age2= 40
# print("actual value:", age2)
# favsub= "maths"
# age2= age1
# print("changed value:" , age2)

# name= input("enter your name")
# print("HELLO", name)

# age= input("enter your age")
# print("your age is ", age)

# pi=3.14

# diameter=float(input("enter diameter of circle"))

# radius= diameter/2
# area_of_circle=pi * radius*radius
# print("the area of circle is",area_of_circle)

# length=float(input("enter length of rec"))
# breadth=float(input("enter breadth of rec"))
# area= length*breadth
# print("your area of rectangle is", area) 

# simple intrest

principle=float(input("enter your principle"))
rate= float(input("enter your rate"))
time= float(input("enter your time"))

SI= principle*rate*time/100

print("your simple interest is",SI)

# Marks calculater

Physics=float(input("enter physics marks"))
Chemistry=float(input("enter chemistry marks"))
Maths=float(input("enter maths marks"))
Computer=float(input("enter computer marks"))
English=float(input("enter english marks"))
Total=Physics+Chemistry+Maths+Computer+English
Percentage= Total/500*100
Average= Total/5
print("Total marks is:", Total)
print(" Your_Percentage:", Percentage)
print("average_marks", Average)
print("DATA TYPE IS",type(Average))


a=int(input("enter number"))
b=float(input("enter number"))
sum= a+b
print("the sum of number is:", sum)
print("data type is:", type(sum)) 

a=int(input("enter number"))
converted_value=float(a)
print("your converted value is",converted_value)
print("data type is:",type(converted_value))

a=10
a+=2
print(a)

a=10
a*=30
print(a)

a=393
a/=3
print(a)

# smart temperature converter
C=int(input("Enter tempreture in Celsius"))
Fahrenheit= (C*9/5)+32
Temp_in_F= float(Fahrenheit)
print("Temp in Fahrenheit is", Temp_in_F)
Kelvin= C + 273.15
Temp_in_C= float(Kelvin)
print("Temp in Kelvin is", Temp_in_C)

# bill calculator

Total_Amount_bill=int(input("Enter Total Bill Amount"))
Number_of_Friends=int(input("Enter how many persons are there"))
Each_person_pay= Total_Amount_bill/Number_of_Friends
Each_person_pay1= float(Each_person_pay)
print("Each person will pay", Each_person_pay1)
print("data type is",type(Total_Amount_bill))
print("data type is", type(Number_of_Friends))
print("data type is",type( Each_person_pay))

# strings

str1= "AyushNegi"
length= len(str1)
print(str1[0])
print(str1[1])
print(str1[2])

# slicing

str="GulabJamaun"
firsthalf=str[0:5]
trialfirsthalf=str[:4]
trialfirsthalf1=str[0:4]
print(firsthalf)
print(trialfirsthalf)
print(trialfirsthalf1) 

str= "cholebhature"
middle_3_char= str[4:7]
print(middle_3_char)

str=input("enter the value")
mid= len(str)//2
output1=str[mid-1:mid+2]
output2=str[-2:]
print(output1)
print(output2)

str="ayushnegi"
print(str.upper())
str="LION"
print(str.lower())

str= "hello world this is ayush negi from mca"
print(str.title())

str="banana"
print(str.find("na"))
str="python is cool and fun language"
print(str.replace("cool","hard"))