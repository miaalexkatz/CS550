#Mia Katz 9/14/18
#This is the effective wind chill temperature calculator, argument 1 is the current temperature in fahrenheit, and the second is the velocity.

import sys
t = float(sys.argv[1])
v = float(sys.argv[2])
w =  35.74  +  0.6215* t  +  (0.4275*t  -  35.75)* v
print("Effective Temperature with Wind Chill:",w)