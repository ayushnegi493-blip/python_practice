# Question 20 → Student Report Card

# Class:

# Student

# Methods:

# addMarks()
# calculateAverage()
# displayResult()

class Student:
    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def addMarks(self,marks1,marks2,marks3):
        totalMarks= marks1+marks2+marks3
        print("Total Marks",totalMarks)
    
    def Average(self,marks1,marks2,marks3):
        avg=(marks1+marks2+marks3)/3
        print("Average Marks",avg)

    def displayResult(self,marks1,marks2,marks3):
        total= marks1+marks2+marks3
        if total>99:
            print("pass")
        else:
            print("fail")


student=Student(78,45,73)
print("Marks",student.marks1)
print("Marks",student.marks2)
print("Marks",student.marks3)

student.addMarks(78,45,73)
student.Average(78,45,73)
student.displayResult(78,45,73)



        
 