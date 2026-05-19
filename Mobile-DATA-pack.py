print("Welcome to Mobile data pack")
data_pack=str(input("enter your data pack 1GB 2GB 3GB"))
Caller_Tune= input("if caller tune needed press Y else N")

bill=0

if data_pack== "1GB":
 bill= 199
elif data_pack=="2GB":
 bill= 299
elif data_pack=="3GB":
 bill= 399
else:
 print("no option available")

if Caller_Tune=="Y":
 bill+= 30
print(f"your total amount is {bill} Rs")







