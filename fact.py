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

def crazyeight(n):
	if n == 0:
		return 0
	if n%10 == 8:
		if n%100 == 88:
			return 2 + crazyeight(n//10)
		return 1 + crazyeight(n//10)
	