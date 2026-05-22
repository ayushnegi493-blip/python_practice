

# file=open("report.txt", "r")
# data= file.read()
# file.close()

# with open("report.txt", "r") as f:
#     data=f.read()
#     print("File data", data)

# with open("newTextfile.txt","r") as f:
#     # line1=f.readline()
#     # line2=f.readline()
#     # line3=f.readline()
#     # data= f.read()

#     # print("Line 1", line1)
#     # print("Line 2",line2)
#     # print("Line3",line3)
#     # print("File Data",data)

#     readLinesMethod=f.readlines()
#     print(readLinesMethod)

# with open("newTextfile.txt","r") as f:
#     line1= f.readline()

#     print("Line->",line1)
    
# print how many lines are present in notes.txt
# with open("newTextfile.txt","r") as f:
#     listofLines= f.readlines()
#     print("Output of readLines Funcitons",listofLines)
#     print('no of lines in file', len(listofLines))

import os
with open("newTextfile.txt","r") as f:
    listofLines= f.readlines()
    print("Output of readLines Funcitons",listofLines)
    print('no of lines in file', len(listofLines))

    # os.rename("certificate.txt","ayush.txt")
    os.remove("mast.txt")
