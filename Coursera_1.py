#Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
 #	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are
 
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

#2. Write a Python program to get the Python version you are using. 
# import sys

# print(sys.version_info)
# print(sys.version)
# print(sys.argv, sys.stdout, sys.stderr)

#3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# import datetime
# now = datetime.datetime.now()
# print("Current date and time :")
# print(now.strftime("%Y-%m-%d %H.%M.%S"))

#4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# from math import pi
# r= int(input("type radius: "))
# area = pi * (r**2)
# print(area)

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# name=input("what is your name?: ")
# sname=input("what is your sname?: ")

# print(sname[::-1],name[::-1])

# def myfunc(x,y):
#     return y, x
# name=input("w is y n?: ")
# sname=input("w is y sn?: ")
# myt=myfunc(name, sname)
# print(myt)

# maindata= input("type numbers with comma: ")
# li = maindata.split()
# print(li, tuple(li))

#7.
filen=input("type your file name: ")
filex = filen.split(".")
print(filex[-1]) 