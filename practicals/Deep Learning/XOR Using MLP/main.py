# main.py
import numpy as np
from functions import sigmoid, sigmoid_derivative, initialize_weights, forward_pass

# Example data
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Hyperparameters
input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 10000

# Initialize weights
weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)

# Training
for epoch in range(epochs):
    # Forward pass
    hidden_layer_activation, predicted_output = forward_pass(inputs, weights_input_hidden, weights_hidden_output)

    # Compute error
    error = outputs - predicted_output
    output_layer_adjustment = error * sigmoid_derivative(predicted_output)
    
    # Backpropagation
    hidden_layer_error = output_layer_adjustment.dot(weights_hidden_output.T)
    hidden_layer_adjustment = hidden_layer_error * sigmoid_derivative(hidden_layer_activation)

    # Update weights
    weights_hidden_output += hidden_layer_activation.T.dot(output_layer_adjustment) * learning_rate
    weights_input_hidden += inputs.T.dot(hidden_layer_adjustment) * learning_rate

print("Trained weights (input to hidden):\n", weights_input_hidden)
print("Trained weights (hidden to output):\n", weights_hidden_output)
print("Predicted output:\n", predicted_output)
