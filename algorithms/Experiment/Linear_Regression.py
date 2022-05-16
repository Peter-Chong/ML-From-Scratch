import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

from algorithms.Utils import train_test_split
from algorithms.Supervised import LinearRegression

def main():
    
    X, y = make_regression(n_features = 1, noise = 20)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    n_samples, n_features = np.shape(X)

    model = LinearRegression(epochs=100)
    model.fit(X_train, y_train)

    print('ok')


if __name__ == "__main__":
    main()