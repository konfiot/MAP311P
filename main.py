import graham
import gen
import matplotlib.pyplot as plt
import scipy.optimize as opt
import statistics
import numpy as np

def f(x, k):
	return k*x**(1/3)

out = []
for i in range(10, 1000):
	out.append(statistics.mean([len(graham.graham(gen.gen3(i))) for k in range(10)]))

plt.xlabel("$n$")
plt.ylabel("$\epsilon_n$")
par, res = opt.curve_fit(f, np.arange(10, 1000), out)
print(par, res)

cmin = min([out[i-10]/i**(1/3) for i in range(10, 1000)])
cmax = max([out[i-10]/i**(1/3) for i in range(10, 1000)])

plt.plot(range(10, 1000), out, label="Data")
plt.plot(range(10, 1000), [f(x, par[0]) for x in range(10, 1000)], label="Least squares approximation")
plt.plot(range(10, 1000), [f(x, cmin) for x in range(10, 1000)], "--", label="cmin")
plt.plot(range(10, 1000), [f(x, cmax) for x in range(10, 1000)], "--", label="cmax")


plt.legend()
plt.show()
