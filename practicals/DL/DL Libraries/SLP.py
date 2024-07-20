import numpy as np

class SingleLayerPerceptron:
    def __init__(self, input_dim, learning_rate=0.01, epochs=100):
        self.input_dim = input_dim
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_dim + 1)  # Including bias weight

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict(self, X):
        # Add bias term to input data
        X_bias = np.c_[np.ones(X.shape[0]), X]
        # Compute the linear combination of inputs and weights
        linear_output = np.dot(X_bias, self.weights)
        # Apply sigmoid activation function
        return self.sigmoid(linear_output)

    def fit(self, X, y):
        # Add bias term to input data
        X_bias = np.c_[np.ones(X.shape[0]), X]
        
        for epoch in range(self.epochs):
            # Compute predictions
            predictions = self.predict(X)
            # Compute errors
            errors = y - predictions
            # Update weights using gradient descent
            self.weights += self.learning_rate * np.dot(X_bias.T, errors)

    def evaluate(self, X, y):
        predictions = self.predict(X)
        predictions_binary = predictions >= 0.5
        accuracy = np.mean(predictions_binary == y)
        return accuracy

# Sample usage
if __name__ == "__main__":
    # Example dataset (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])  # XOR output

    # Create and train the model
    slp = SingleLayerPerceptron(input_dim=2, learning_rate=0.1, epochs=1000)
    slp.fit(X, y)

    # Evaluate the model
    accuracy = slp.evaluate(X, y)
    print(f"Accuracy: {accuracy * 100:.2f}%")
