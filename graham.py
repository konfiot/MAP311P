#!/usr/bin/python3
# -*- coding: utf-8 -*-

from cmath import *
import math
import random

def vecteur(A, B, C):
	return (B[0] - A[0])*(C[1] - A[1]) - (C[0] - A[0])*(B[1] - A[1])


def graham(points):
	out = []

	gauche = min(points, key=lambda x: x[0]) # Choix du pivot initial : Le point le plus a gauche

	#print(gauche)
	out.append(gauche) # On retire ce point du tableau
	points.remove(gauche)

	points.sort(key = lambda x: math.atan2((x[1]-gauche[1]),  (x[0]-gauche[0]))) # Tri par rapport a la pente formée par la droite (extrema - point comparé), décrit un tour dans le sens inverse des aiguilles d'une montre car l'extrema considéré est le point le plus a gauche

	#print(points)
	#print(phase(complex(*gauche)))
	#print([math.atan2((x[1]-gauche[1]),  (x[0]-gauche[0])) for x in points])

	out.append(points[0]) # On ajoute le point avec la pente la plus faible (on tourne à gauche)

	for i in range(1, len(points)):
		#print(out)
		while vecteur(out[-2], out[-1], points[i]) <= 0:
			out.pop()
		out.append(points[i])
	
	return out

if __name__ == "__main__":
	print(graham([(-1,-1), (1,-1), (-1, 1), (1, 1)])) # Cas trivial, carré
	print(graham([(-1,-1), (1,-1), (-1, 1), (1, 1), (0, 0)])) # On rajoute un point au milieu
	print(graham([(-1,-1), (1,-1), (-1, 1), (1, 1), (.5, .5)])) # Deux points alignés par rapport au premier pivot ==> Meme pente dans le tri initial

	test = [(2*random.random()-1, 2*random.random()-1) for i in range(100)]
	test += [(-2,-2), (-2,2), (2,-2), (2,2)]
	print(graham(test)) # Points aléatoires contenus dans un carré 4x4
