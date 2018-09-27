import random
t=[]
for i in range(10):
	t.append(random.randrange(100))
t.sort(reverse = True)
for i in range(len(t)-1): 
	if t[i-1]%3 == 0:
		t.remove(i-3)


	
print(t)