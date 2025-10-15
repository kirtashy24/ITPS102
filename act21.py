import random 

print("WE GON TO LASVEGAS")
print("===========================================")

ran = random.randint(1,10)
tries = 0
tuloy = True

name = input("Enter your name >")

while tuloy == True:
    num = eval(input("Input your number >"))
    tries += 1 
    if num == ran:
        print ("Bongga ka Bakla!!!")
        break

    else:
        print ("Opss, waleyy")
        continue

print(f"Hi {name}, you got the correct number!! \n Number of tries : {tries}")