import random
import matplotlib.pyplot as plt
def calorieparty():
	calories = 0
	parties = random.randrange(1, 13)
	for i in range(parties):
		desserts = random.randrange(1,8)
		for i in range(desserts):
			calories += random.randrange(40, 500)
	return calories

graph = []
for i in range(52001):
	graph.append(0)

for i in range(1000000):
	graph[calorieparty()] += 1
plt.plot(graph)
plt.show()

