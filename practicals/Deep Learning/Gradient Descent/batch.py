def batch_gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    cost_history = np.zeros(num_iterations)
    for i in range(num_iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradients = (1 / m) * X.T.dot(errors)
        theta = theta - learning_rate * gradients
        cost_history[i] = compute_cost(X, y, theta)
    return theta, cost_history

theta, cost_history = batch_gradient_descent(X, y, theta, learning_rate, num_iterations)

print("Theta:", theta)
print("Final cost:", cost_history[-1])

plt.plot(range(num_iterations), cost_history, color='blue')
plt.xlabel('Number of iterations')
plt.ylabel('Cost')
plt.title('Cost Function Over Iterations')
plt.grid(True)
plt.show()