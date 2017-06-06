# -*- coding: utf-8 -*-
import graham
import gen
import statistics
import sys

filename = 'out_' + sys.argv[1] + '.csv'

with open(filename, "w") as f:
	out = []
	for i in range(10, 1000):
		out.append(statistics.mean([len(graham.graham(gen.genppoly(int(sys.argv[1]), i))) for k in range(100)]))

	f.write(",".join(map(str, out)))
