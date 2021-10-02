try:    
     number = int(input("Which number do you want to check? "))
except:
     print("please enter anumber")
if number%2 == 0:
     print("This is an Even Number")
else:
    print("This is a Odd Number")
