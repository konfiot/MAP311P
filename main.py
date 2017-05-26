import graham
import gen
import matplotlib.pyplot as plt
import statistics

out = []
for i in range(10, 1000):
	out.append(statistics.mean([len(graham.graham(gen.gen3(i))) for k in range(100)]))

plt.plot(range(10, 1000), out)
plt.show()
