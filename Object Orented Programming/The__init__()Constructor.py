# class Student:
#     schoolName="ABC School"
#     def __init__(self):
#         print("Whenever a new object is created I am called automatically")
#         print(self)

# student1=Student() #init method will be called
# print(student1.schoolName)
# print("Student1",student1)

# student2=Student()


class Student:
    schoolName="ABC School"
    def __init__(self,name,course):
        # print("Whenever a new object is created I am called automatically")
        # print(self)
        self.name=name
        self.course=course

        

student1=Student("kushi","BCA") #init method will be called
print(student1.schoolName)
print("Student1 Name",student1.name)
print("Student Course",student1.course)

student2=Student("ankit","BSC")
print(student2.schoolName)
print("Student2 Name",student2.name)
print("Student2 Course",student2.course)


    