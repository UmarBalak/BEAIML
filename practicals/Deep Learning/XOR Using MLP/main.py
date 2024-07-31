from functions import *

# XOR Logic Function
def XOR_logic(x):
	y1 = AND_logic(x)
	y2 = OR_logic(x)
	y3 = NOT_logic(y1)
	final_x = np.array([y2, y3])
	finalOutput = AND_logic(final_x)
	return finalOutput

# testing the Perceptron Model
test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for i in test:
	print("XOR({}, {}) = {}".format(i[0], i[1], XOR_logic(i)))

