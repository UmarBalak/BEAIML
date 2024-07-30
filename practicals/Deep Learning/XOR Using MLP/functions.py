import numpy as np

# weights
w = np.array([1, 1]) # Weighst for AND and OR gate
wNOT = -1

# biases
bNOT = 0.5
bAND = -1.5
bOR = -0.5

def unitStep_activation(v):
	if v >= 0:
		return 1
	else:
		return 0

def dot_activation(x, w, b):
	v = np.dot(w, x) + b
	y = unitStep_activation(v)
	return y

def NOT_logicFunction(x):
	return dot_activation(x, wNOT, bNOT)

def AND_logicFunction(x):
	return dot_activation(x, w, bAND)

def OR_logicFunction(x):
	return dot_activation(x, w, bOR)


