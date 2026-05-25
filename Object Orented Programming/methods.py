class Vehicle:
    color="black"
    petrolordiesal="petrol"
    mileage="60"

    def start():
        print("When your press clutch and accelerator then vehicle is start")


car=Vehicle()
car.color="red"
print(car.color)


bike= Vehicle()
bike.color="Green"
print(bike.color)


# class Instructor:
#     followers=0   #class variable
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def display(self):
#         print(f"hyy I am {self.name}")

# instructor_1=Instructor("pyush","Dehradun")
# print(instructor_1.name)
# print(instructor_1.followers)

# instructor_2=Instructor("rima","Tehri")
# print(instructor_2.name)
# print(instructor_2.address)
# # print(instructor_1.display())
# instructor_1.display() 

# Q1 Create class Student that takes 3 marks and has method average

class Student:
    

    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def average(self,marks1,marks2,marks3):
        avg=(marks1+marks2+marks3)/3
        print("Average Marks",avg)



Aditya=Student(56,67,96)
print(Aditya.marks1)
print(Aditya.marks2)
print(Aditya.marks3)

Aditya.average(56,67,96)


Kushi= Student(89,54,95)
print(Kushi.marks1)
print(Kushi.marks2) 
print(Kushi.marks3)

Kushi.average(89,54,95)
        


# Question 17 → Exam Result

# Class:

# Exam

# Method:

# result()

# If all marks > 33:

# Pass

# Otherwise:

# Fail


class Exam:
    def __init__(self,marks):
        self.marks=marks

    def result(self,marks):
        if marks>= 33:
            print("pass")
        else:
            print("fail")


exam=Exam(13)
print("Marks",exam.marks)

exam.result(13)


# Question 16 → Instagram Followers

# Class:

# Influencer

# Method:

# followersGrowth()

# If followers increase > 1000:

# Viral Creator

# Else:

# Growing Creator


class Influencer:
    def __init__(self,followers):
        self.followers=followers

    def influencer(self,followers):
        if followers > 1000:
            print("Viral Creator")
        else:
            print("Growing Creator")

person=Influencer(983)
print("Followers",person.followers)
person.influencer(983)



        




        