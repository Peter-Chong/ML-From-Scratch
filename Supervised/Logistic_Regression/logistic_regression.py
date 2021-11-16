import math
import numpy as np

class LogisticRegression:
    def __init__(self):
        pass
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def fit(self, X, y, learning_rate = 0.01, num_iter = 5000):
        n_features = np.shape(X)[1]

        # 1) Create random initial thetas of size (n_features, 1)
        temp = 1/math.sqrt(n_features)
        self.thetas = np.random.uniform(-temp, temp, (n_features,))

        # 2) Tune the theta for num_iter times
        for i in range(num_iter):
            # 2.1) Make new prediction
            y_pred = self.sigmoid(X.dot(self.thetas))
            # 2.2) Update thetas
            self.thetas -= learning_rate * -(y - y_pred).dot(X)

    def predict(self, X, prob=False):
        y_pred = self.sigmoid(X.dot(self.thetas))
        if prob:
            return y_pred
        return np.round(y_pred).astype(int)
