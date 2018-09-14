#Mia Katz 9/14/18
#The x<y<z true or false program, it took me some research time to realize that && means nothing in Python
#Thank you to docs.python.org for the help on if statements and compound statements! 
import sys
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
if x < y < z:
	print("True")
elif z < y < x:
	print("True")
else:
	print("False")