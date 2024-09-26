import tensorflow as tf
from keras.layers import Input, Dense, Flatten, Reshape, Conv2D, Conv2DTranspose, UpSampling2D
from keras.models import Model
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]


# Encoder
input_img = Input(shape=(28, 28, 1))

x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = Flatten()(x)

# Bottleneck layer
encoded = Dense(16, activation='relu')(x)

# Decoder
x = Dense(7 * 7 * 64, activation='relu')(encoded)
x = Reshape((7, 7, 64))(x)
x = Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x) # Upsample to (14, 14)
x = Conv2DTranspose(32, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x) # Upsample to (28, 28)
decoded = Conv2DTranspose(1, (3, 3), activation='sigmoid', padding='same')(x)

# Create the autoencoder model
autoencoder = Model(input_img, decoded)

# Compile the model
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Train the autoencoder
autoencoder.fit(x_train, x_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))

# Evaluate the autoencoder
loss = autoencoder.evaluate(x_test, x_test)
print(f'Test Loss: {loss}')

decoded_imgs = autoencoder.predict(x_test)

# Optional (to plot the actual and predicted images)
def plot_images(original_images, reconstructed_images, num_images=10):
    plt.figure(figsize=(20, 4))
    for i in range(num_images):

        ax = plt.subplot(2, num_images, i + 1)
        plt.imshow(original_images[i].reshape(28, 28), cmap='gray')
        plt.title("Original")
        plt.gray()
        plt.axis('off')

        ax = plt.subplot(2, num_images, i + 1 + num_images)
        plt.imshow(reconstructed_images[i].reshape(28, 28), cmap='gray')
        plt.title("Reconstructed")
        plt.gray()
        plt.axis('off')

    plt.show()

plot_images(x_test, decoded_imgs)