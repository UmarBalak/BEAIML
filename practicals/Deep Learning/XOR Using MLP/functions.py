import numpy as np

def unitStep(v):
	if v >= 0:
		return 1
	else:
		return 0

def perceptronModel(x, w, b):
	v = np.dot(w, x) + b
	y = unitStep(v)
	return y

# NOT Logic Function
# wNOT = -1, bNOT = 0.5
def NOT_logicFunction(x):
	wNOT = -1
	bNOT = 0.5
	return perceptronModel(x, wNOT, bNOT)

# AND Logic Function
# here w1 = wAND1 = 1, 
# w2 = wAND2 = 1, bAND = -1.5
def AND_logicFunction(x):
	w = np.array([1, 1])
	bAND = -1.5
	return perceptronModel(x, w, bAND)

# OR Logic Function
# w1 = 1, w2 = 1, bOR = -0.5
def OR_logicFunction(x):
	w = np.array([1, 1])
	bOR = -0.5
	return perceptronModel(x, w, bOR)


