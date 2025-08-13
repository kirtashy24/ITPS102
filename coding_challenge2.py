rcm = eval(input("Magkano Cash-Out mo? > "))

cm = rcm

a = cm // 1000
cm = cm % 1000

b = cm // 500
cm = cm % 500

c = cm // 200
cm = cm % 200

d = cm // 100
cm = cm % 100

e = cm // 50
cm = cm % 50

f = cm // 20
cm = cm % 20

g = cm // 10
cm = cm % 10

h = cm // 5
cm = cm % 5

i = cm // 1
cm = cm % 1

print("\n\t\tYour current breakdown is:")
print("\t\t\t",a, "\t- 1000")
print("\t\t\t",b, "\t- 500")
print("\t\t\t",c, "\t- 200")
print("\t\t\t",d, "\t- 100")
print("\t\t\t",e, "\t- 50")
print("\t\t\t",f, "\t- 20")
print("\t\t\t",g, "\t- 10")
print("\t\t\t",h, "\t- 5")
print("\t\t\t",i, "\t- 1")

com = eval(input("Magkano Cash-Out mo? > "))

print("Your current balance is" , rcm - com)