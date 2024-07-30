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
test1 = np.array([0, 0])
test2 = np.array([0, 1])
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("XOR({}, {}) = {}".format(0, 0, XOR_logicFunction(test1)))
print("XOR({}, {}) = {}".format(0, 1, XOR_logicFunction(test2)))
print("XOR({}, {}) = {}".format(1, 0, XOR_logicFunction(test3)))
print("XOR({}, {}) = {}".format(1, 1, XOR_logicFunction(test4)))