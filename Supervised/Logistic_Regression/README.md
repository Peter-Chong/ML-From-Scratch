# Logistic Regression

Logistic regression fits x into a sigmoid function and classify them as 0 if the output is < 0.5 and 1 otherwise.

## Sigmoid Function
This function maps any real value into another value between 0 and 1.  
![equation](https://latex.codecogs.com/gif.latex?h%28z%29%20%3D%20%5Cfrac%7B1%7D%7B1&plus;%5Cexp%5E%7B-z%7D%7D)  
where  
![equation](https://latex.codecogs.com/gif.latex?z%20%3D%20%5Ctheta_0%20x_0%20&plus;%20%5Ctheta_1%20x_1%20&plus;%20%5Ctheta_2%20x_2%20&plus;%20...%20%5Ctheta_N%20x_N)  

In order to train the weights (thetas) in the sigmoid function, we need to minimize a cost function.

## Cost Function
A cost function represents optimization objective i.e. we create a cost function and minimize it so that we can develop an accurate model with minimum error.  
![equation](https://latex.codecogs.com/gif.latex?J%28%5Ctheta%29%20%3D%20-%5Cfrac%7B1%7D%7Bm%7D%20%5Csum_%7Bi%3D1%7D%5Em%20y%5E%7B%28i%29%7D%5Clog%20%28h%28z%28%5Ctheta%29%5E%7B%28i%29%7D%29%29%20&plus;%20%281-y%5E%7B%28i%29%7D%29%5Clog%20%281-h%28z%28%5Ctheta%29%5E%7B%28i%29%7D%29%29)

## Gradient Descent
We minimize the above cost function using gradient descent.  
To update the weight, we adjust it by subtracting a fraction of the gradient determined by learning rate (alpha)

![equation](https://latex.codecogs.com/gif.latex?%5Ctheta_j%20%3D%20%5Ctheta_j%20-%20%5Calpha%20%5Ctimes%20%5Cnabla_%7B%5Ctheta_j%7DJ%28%5Ctheta%29)

where the gradient of the our cost function is  
![equation](https://latex.codecogs.com/gif.latex?%5Cnabla_%7B%5Ctheta_j%7DJ%28%5Ctheta%29%20%3D%20%5Cfrac%7B1%7D%7Bm%7D%20%5Csum_%7Bi%3D1%7D%5Em%28h%5E%7B%28i%29%7D-y%5E%7B%28i%29%7D%29x%5E%7B%28i%29%7D_j)  

In a matrix format:  
![equation](https://latex.codecogs.com/gif.latex?%5Ctheta%20%3D%20%5Ctheta%20-%20%5Cfrac%7B%5Calpha%7D%7Bm%7D%20%5Ctimes%20%28x%5E%7BT%7D%20%5Ccdot%20%28h-y%29%29)

