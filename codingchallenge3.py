name = input("\nWhat is your name? :")
age = input("How old are you? :")
fair = eval(input("How much is your pamasahe :"))
student= input("Are you a student? :")


if student.lower() == "yes":
	dis = fair * 0.2
	nfair = fair - dis
	print("\n\tHello,", name , ", bibigyan ka ng discount! Mga", dis)
	print("\tSo ang magiging pamasahe mo ay", nfair)
else:
	print("\n\tNo madupang allowed!!!")