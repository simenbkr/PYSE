#!/usr/bin/python

#import numpy as np
files = ['simpsons.B', 'simpsons.I', 'simpsons.P']
combined = 'simpsons.IPB'


def sampleMean(lista):
	return sum(lista)/float(len(lista))

def sampleVar(lista):
	s = 0
	n = len(lista)
	mean = sampleMean(lista)

	for num in lista:
		#s += num ** 2 - float(len(lista) / (len(lista) - 1)) * sampleMean(lista) ** 2
		s += (num - mean) ** 2

	return s * (1/float(n - 1))

def showMeanAndVar():
	files = ['simpsons.B', 'simpsons.I', 'simpsons.P']

	for fila in files:

		with open(fila, 'r') as f:

			nums = [int(x.strip().replace('\n', '')) for x in f.readlines()]
			#print nums
			mean = sampleMean(nums)
			var = sampleVar(nums)
			f.close()

			print "{} mean: {}".format(fila, mean)
			print "{} var: {}".format(fila, var)


import numpy as np
import math
import scipy.stats as stats
import pylab as pl

def taskCI():
	iframes = 'simpsons.IPB'
	nums = [int(x.strip().replace('\n','')) for x in open(iframes, 'r').readlines()]
	nums = sorted(nums)
	mean = sampleMean(nums)
	var = sampleVar(nums)
	std = math.sqrt(var)
	
	fit = stats.norm.pdf(nums, mean, std)

	pl.plot(nums, fit, '-o')
	pl.hist(nums, normed=True)
	pl.show()


def p(j, mean, lista):
	n = len(lista)
	p = 0
	div = 0
	for i in range(n-j):
		p += float(lista[i] - mean) * (lista[i+j] - mean)
		div += float(lista[i] - mean) ** 2


	#print p, div
	p = p/div
	p = p * n
	p = p/(n - j)

	return p

def taskD(fila, k):

	lista =  [int(x.strip().replace('\n','')) for x in open(fila, 'r').readlines()]
	mean = sampleMean(lista)
	for i in range(k):
		print "{} has p of {}".format(i, p(i, mean, lista))

taskD('simpsons.IPB', 100)




