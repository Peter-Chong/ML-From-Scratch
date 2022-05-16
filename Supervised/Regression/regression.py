from functools import lru_cache
import math
import numpy as np

class LinearRegression:
    """
    Parameters
    -------------
    learning_rate: float
        The step length that will used when updating the weights
    epochs: int
        The number of training iterations
    """
    def __init__(self, learning_rate = 0.1, epochs = 1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
    
    def initialize_weights(self, n_features):
        self.

    def fit(self, X, y):
        m, n = X.shape

        # Initialize weights and bias
        self.weights = np.zeros((n,1))
        self.bias = 0

        # Reshaping y
        y = y.reshape(m, 1)

        # Empty list to store losses
        self.losses = []

        # Gradient descent
        for epoch in range(self.epochs):
            # Calculate prediction
            y_hat = np.dot(X, self.weights) + self.bias
            
            # Calculate loss
            loss = np.mean((y_hat - y)**2)
            self.losses.append(loss)

            # Calculate derivatives
            dw = (1/m)*np.dot(X.T, (y_hat - y))
            db = (1/m)*np.sum((y_hat - y))

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
        
        return self.weights, self.bias, self.losses
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias