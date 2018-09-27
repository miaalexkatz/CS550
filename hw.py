#Mia Katz
#Group Homework Problems
#Sources: renegadecoder.com, for the list adding in the third problem

#Shuffle numbers 1 to 100
import random
import sys
x = [i for i in range(100)]
random.shuffle(x)
print("100 shuffled numbers:",x)

#Print 10 random numbers, order them descending, remove multiples of 3
t=[]
for i in range(10):
	r = (random.randrange(100))
	t.append(r)
	if r%3 == 0:
		t.remove(r)
t.sort(reverse = True)

print("10 numbers, minus those divisible by 3:",t)

#take ten arguments, print them in order, in reverse order, and the sum
l = []
m = []
for i in range(1,11):
	p = int(sys.argv[i])
	l.append(p)
	m.append(p)
l.sort()
print(l)
m.sort(reverse = True)
print(m)
al = [sum(pair) for pair in zip(l, m)]
print("Sum of both lists:",al)



