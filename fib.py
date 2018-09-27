import sys
i = sys.argv[1]
i = int(i)
def fib(n):
	a = 1
	b = 1
	for n in range(0,i):
		n = n+1
		a = b
		b = a+b
		return a 
	print(a)

fib(i)

