import math
x = input("Enter a Number ")
x = math.radians(float(x))
y = math.sin(float(x))**2 + math.cos(float(x))**2
print(y)