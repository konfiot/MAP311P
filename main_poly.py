import graham
import gen
import matplotlib.pyplot as plt
import scipy.optimize as opt
import statistics
import numpy as np

GAMMA = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495

def f(x, k):
	#return k*x**(1/3)
	return k*(np.log(x/2) + GAMMA)

out = []
for i in range(10, 1000):
	out.append(statistics.mean([len(graham.graham(gen.genppoly(5, i))) for k in range(10)]))

plt.xlabel("$n$")
plt.ylabel("$\epsilon_n$")
par, res = opt.curve_fit(f, np.arange(10, 1000), out)
print(par, res)


plt.plot(range(10, 1000), out, label="Data")
plt.plot(range(10, 1000), [f(x, par[0]) for x in range(10, 1000)], label="Least squares approximation")


plt.legend()
plt.show()
