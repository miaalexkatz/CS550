#Mia Kat 9.4.18
#Day of the week
#It's been an hour, and I've been having a lot of problems getting the formula to work properly 
#I'm not sure why the formula is  behaving this way? I was only able to find date-time related solutions online.

import sys
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y0 = int(y -(14  -  m)/  12)
x  = int(y0 +y0/4 -y0/100+y0/400) 
m0 = int(m  +  12  *  ((14  -  m) / 12)  -  2)  
d0 = int(d  +  x  +  (31*m0)/12) %7 

print("The Day of the Week is... ")
if d0 == 0:
	print("Sunday")
elif d0 == 1:
	print("Monday")
elif d0 == 2:
	print("Tuesday")
elif d0 == 3:
	print("Wednesday")
elif d0 == 4:
	print("Thursday")
elif d0 == 5:
	print("Friday")
else:
	print("Saturday")