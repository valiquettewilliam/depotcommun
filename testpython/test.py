# -*-coding:utf-8 -*
#~/Téléchargements/python3.6

a = input("Saisissez une année : "	)
if a%4 != 0:
	print("nope fuck you")
elif a%100 == 0:
	if a%400 == 0:
		print("yep but fuck you anyway")
	else :
		print("nope fuck you")
else : 
	print("yep but fuck you anyway")


	
