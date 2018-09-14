#Mia Katz 9/14/18
#This is the effective wind chill temperature calculator, argument 1 is the current temperature in fahrenheit, and the second is the velocity.

import sys
t = int(sys.argv[1])
v = int(sys.argv[2])
w = float(35.74  +  (0.6215* t)  +  ((0.4275*t*v) - (35.75) *v**0.16)	
print("Temperature with Wind Chill:",w " Degrees F")