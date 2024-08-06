def mini_batch_gradient_descent(X, y, theta, learning_rate, num_iterations, batch_size):
    m = len(y)
    cost_history = np.zeros(num_iterations)
    for i in range(num_iterations):
        indices = np.random.permutation(m)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        for start in range(0, m, batch_size):
            end = min(start + batch_size, m)
            X_mini_batch = X_shuffled[start:end]
            y_mini_batch = y_shuffled[start:end]
            predictions = X_mini_batch.dot(theta)
            errors = predictions - y_mini_batch
            gradients = (1 / len(y_mini_batch)) * X_mini_batch.T.dot(errors)
            theta = theta - learning_rate * gradients
        cost_history[i] = compute_cost(X, y, theta)
    return theta, cost_history

batch_size = 64
theta, cost_history = mini_batch_gradient_descent(X, y, theta, learning_rate, num_iterations, batch_size)
print("Theta:", theta)
print("Final cost:", cost_history[-1])

plt.plot(range(num_iterations), cost_history, color='blue')
plt.xlabel('Number of iterations')
plt.ylabel('Cost')
plt.title('Cost Function Over Iterations (Mini-Batch Gradient Descent)')
plt.grid(True)
plt.show()