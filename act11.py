dec = eval(input("How loud is it --->"))

if dec <= 20 and dec >= 1:
	print("Little too soft")

elif dec >= 21 and dec <= 40:
	print("Too soft")

elif dec >= 41 and dec <= 60:
	print("Normal")

elif dec >= 61 and dec <= 80:
	print("A bit loud")

elif dec >= 81 and dec <= 100 :
	print("Too soft")

else :
	print("Danggggg")
