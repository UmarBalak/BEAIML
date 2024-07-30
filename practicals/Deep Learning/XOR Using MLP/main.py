from functions import *

# XOR Logic Function
def XOR_logicFunction(x):
	y1 = AND_logicFunction(x)
	y2 = OR_logicFunction(x)
	y3 = NOT_logicFunction(y1)
	final_x = np.array([y2, y3])
	finalOutput = AND_logicFunction(final_x)
	return finalOutput

# testing the Perceptron Model
test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for i in test:
	print("XOR({}, {}) = {}".format(i[0], i[1], XOR_logicFunction(i)))

