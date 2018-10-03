i = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print(i[0][0])
j = []
for x in range(10):
	j.append(0)
#or
j = [0]*10
#they're literally the same thing!
k = [[0]*10 for x in range(10)]
print(k)

for x in range(len(k)):
	print(*k[x])
#star gets rid of brakcet notation