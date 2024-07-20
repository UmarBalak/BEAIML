# utils.py
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_weights(input_size, hidden_size, output_size):
    weights_input_hidden = np.random.rand(input_size, hidden_size)
    weights_hidden_output = np.random.rand(hidden_size, output_size)
    return weights_input_hidden, weights_hidden_output

def forward_pass(inputs, weights_input_hidden, weights_hidden_output):
    hidden_layer_activation = sigmoid(np.dot(inputs, weights_input_hidden))
    output_layer_activation = sigmoid(np.dot(hidden_layer_activation, weights_hidden_output))
    return hidden_layer_activation, output_layer_activation
