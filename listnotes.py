a = []
#add something to list
a.append(4)
a.append(3)
a.insert(1,0)
print(a)


c, b = 7, 5
b, c = c, b

#or


e = [1, 2, 3, 7, 5, 6, 4]
e[4], e[6] = e[6], e[4]

f = []

for i in range(0, 700, 7):
	f.append(i)
print(f)

import random
g = []
for i in range(10):
	g.append(random.randrange(0,100))
	i += 1
print(g)
#sort doesn't return anything, so they must be separate
g.sort()
print(g)