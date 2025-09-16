from getpass import getpass

uname = 'kiroash'
pword = 'notashy24'

u = input("Username :")
p = getpass("Password :")

if (u == uname) and (p == pword):
	print("\tTumpak, you may enter")

else :
	print("\tHala bawal ka")