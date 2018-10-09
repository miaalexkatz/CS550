def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*fact(n-1)
print(fact(5))

use = input("enter a string: ")
global xcount
xcount = 0
def countx(user):
	global xcount
	for x in user:
		if x is "x":
			xcount += 1
			
	return xcount

print("number of xs:",countx(use))

eight = input("enter whatever the heck you want: ")
global ecount 
ecount = 0
def eco(ei):
	global ecount
	val = "hi"
	for x in eight:
		if val is "8":
			ecount += 1
		if x is "8":
			ecount += 1
		val = str(x)

	return ecount
print("crazy eights:",eco(eight))

eu = input("first for gcd")
eu2 = input("next for gcd")
g
