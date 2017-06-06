# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np


GAMMA = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495

def func(x, k):
	#return k*x**(1/3)
	return k*(np.log(x/2) + GAMMA)


out = []

for i in range(3, 500):
	try:
		f = open("out_" + str(i) + ".csv", "r")
		l = f.readline()
		data = list(map(float, l.split(",")))
		par, res = opt.curve_fit(func, np.arange(10, 1000), data)
		out.append(par[0])
	except FileNotFoundError:
		print("FIchier " + str(i) + " non trouvé")

plt.plot(range(3, 493), out)
plt.show()
