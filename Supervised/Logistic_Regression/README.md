# Logistic Regression

Logistic regression fits x into a sigmoid function and classify them as 0 if the output is < 0.5 and 1 otherwise.

## Sigmoid Function
This function maps any real value into another value between 0 and 1.  
![equation](https://latex.codecogs.com/gif.latex?%5Csigma%28z%29%20%3D%20%5Cfrac%7B1%7D%7B1&plus;e%5E%7B-z%7D%7D)

In order to train the thetas in the sigmoid function, we minimize a cost function

## Cost Function
A cost function represents optimization objective i.e. we create a cost function and minimize it so that we can develop an accurate model with minimum error.
![equation](https://latex.codecogs.com/gif.latex?J%28%5Ctheta%29%20%3D%20-%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7Dy%5E%7B%28i%29%7Dlog%28h%28z%28%5Ctheta%29%5E%7B%7Bi%7D%7D%29%29&plus;%20%281-y%5E%7B%28i%29%7D%29log%281-%20h%28z%28%5Ctheta%29%5E%7B%7Bi%7D%7D%29%29)

## Gradient Descent
We minimize the above cost function using gradient descent.  
The gradient of the above cost function is
