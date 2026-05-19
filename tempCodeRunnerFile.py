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
