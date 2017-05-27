import graham
import gen
import matplotlib.pyplot as plt
#import scipy
import statistics

out = []
for i in range(10, 1000):
	out.append(statistics.mean([len(graham.graham(gen.gen3(i))) for k in range(100)]))

plt.xlabel("$n$")
plt.ylabel("$\epsilon_n$")
plt.plot(range(10, 1000), out)


plt.show()
