#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import math
import cmath


def gen1(n):
	out = []
	for i in range(n):
		r = random.random()
		t = 2*math.pi*random.random()
		out.append((t, r))

	return out

def gen2(n):
	out = []
	while len(out) < n:
		x = 2*random.random()-1
		y = 2*random.random()-1

		if x**2 + y**2 <= 1:
			out.append((x,y))

	return out

def gen3(n):
	out = []
	for i in range(n):
		r = random.random()
		t = 2*math.pi*random.random()
		out.append((math.sqrt(r)*math.cos(t), math.sqrt(r)*math.sin(t)))
	return out

def genppoly(k, n):
	if k < 3:
		return False

	out = []
	for i in range(n):
		i = random.randint(0, k-1)

		l, m = random.random(), random.random()
		rand = l + m*cmath.exp(2j*math.pi/k)

		if l + m > 1:
			rand = -rand + 1 + cmath.exp(2j*math.pi/k)

		

		rand *= cmath.exp(2j*math.pi*i/k)

		out.append((rand.real, rand.imag))

	return out

def test():
	N = 600


	T = []
	r = []
	for i in range(N):
		t = time.time()
		r = gen1(N)
		T.append(time.time() - t)
	print("T1 = " + str(statistics.mean(T) * 1000) + " ms (std.dev. " + str(statistics.stdev(T)*1000) + ")")

	#for (t, r) in r:							# Quand on est parti en WE sans internet et sans matplotlib, on fait comme on peux... C'est a dire avec libreoffice calc...
	#	print(str(r*math.cos(t)) + "," + str(r*math.sin(t)))
	plt.figure(1)
	plt.polar(*zip(*r), marker=".", linestyle='')


	T = []
	r = []
	for i in range(N):
		t = time.time()
		r = gen2(N)
		T.append(time.time() - t)
	print("T2 = " + str(statistics.mean(T) * 1000) + " ms (std.dev. " + str(statistics.stdev(T)*1000) + ")")

	#for (x, y) in r:
	#	print(str(x) + "," + str(y))
	plt.figure(2)
	plt.scatter(*zip(*r), marker=".")


	T = []
	r = []
	for i in range(N):
		t = time.time()
		r = gen3(N)
		T.append(time.time() - t)
	print("T3 = " + str(statistics.mean(T) * 1000) + " ms (std.dev. " + str(statistics.stdev(T)*1000) + ")")


	#for (x, y) in r:
	#	print(str(x) + "," + str(y))
	plt.figure(3)
	plt.scatter(*zip(*r), marker=".")

	T = []
	r = []
	for i in range(N):
		t = time.time()
		r = genppoly(5, N)
		T.append(time.time() - t)
	print("T4 = " + str(statistics.mean(T) * 1000) + " ms (std.dev. " + str(statistics.stdev(T)*1000) + ")")


	#for (x, y) in r:
	#	print(str(x) + "," + str(y))
	plt.figure(4)
	plt.scatter(*zip(*r), marker=".")

	plt.show()
if __name__ == "__main__":
	import time
	import statistics
	import matplotlib.pyplot as plt

	test()
