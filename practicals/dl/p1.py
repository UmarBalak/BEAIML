import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# XOR input data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# XOR output data
y = np.array([[0], [1], [1], [0]])

# Define the model
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))  # Hidden layer with 8 neurons
model.add(Dense(1, activation='sigmoid'))  # Output layer

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Predict using the model
predictions = model.predict(X)
print('Predictions:')
print(np.round(predictions).astype(int))
