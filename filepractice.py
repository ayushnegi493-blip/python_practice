
# Quesiton1
# file= open("notes.txt","r")
# data=file.read()
# data=data.lower()

# print("Data file->",data)
# file.close()

# Question2
# with open("notes.txt",'r') as f:
#     data=f.read()
#     data=data.lower()

#     countItems= len(data)
#     words=data.split()
    
#     countwords= len(words)


#     print("dataFile->",data)
#     print('total letters',countItems)
#     print("Total words",countwords)

# with open("notes.txt","r") as f:
#     no_of_lines=f.readlines()

#     print("Output", no_of_lines)
#     print("Total lines",len(no_of_lines))


# with open("notes.txt",'r') as f:
#     line1= f.readline()
#     line2=f.readline()
#     line3= f.readline()

#     data= f.readline()


#     print("Line1",line1)
#     print("Line2",line2)
#     print("Line3",line3)
#     print("Data file",data)


with open("notes.txt","r") as f:
    data= f.read()
    data= data.lower()
    print("Data file->",data)

    if "master" in data:
        print("yes available")

    else:
        print("not available")






