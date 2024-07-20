# main.py
import numpy as np
from functions import sigmoid, sigmoid_derivative

# Example data
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Initialize weights
input_layer_size = 2
output_layer_size = 1
weights = np.random.rand(input_layer_size, output_layer_size)
bias = np.random.rand(output_layer_size)

# Training
learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # Forward pass
    net_input = np.dot(inputs, weights) + bias
    predicted_output = sigmoid(net_input)

    # Compute error
    error = outputs - predicted_output
    adjustment = error * sigmoid_derivative(predicted_output)

    # Update weights and bias
    weights += np.dot(inputs.T, adjustment) * learning_rate
    bias += np.sum(adjustment, axis=0) * learning_rate

print("Trained weights:\n", weights)
print("Trained bias:\n", bias)
print("Predicted output:\n", predicted_output)
