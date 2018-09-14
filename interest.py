import sys
import math
p = int(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

e = math.e

ex = (r*t)

i =  p* (e**ex)

print("Your Future Value is:",i)