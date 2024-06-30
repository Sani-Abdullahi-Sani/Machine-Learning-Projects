This repository contains two Tasks for the Adaptive Computation and Machine Learning (ACML) Module. Each task is implemented in Python and is described below.

**Task 1: Implementing a Neural Network**

*Description:*
This Task involves creating a Python program that implements a neural network with the following specifications:

1. Input layer with 4 nodes
2. Hidden layer with 8 nodes
3. Output layer with 3 nodes
4. Sigmoid activation function for hidden and output layers
5. Weights and biases initialized to 1

*Features*
1. Feedforward step to compute the network's output for given inputs.
2. Sum-of-squares loss computation between the network's output and target values.
3. Backpropagation method for updating weights and biases with a learning rate of 0.1.

**Task 2: Implementing the k-means Algorithm**

*Description*
This Task involves creating a Python program that implements the k-means algorithm with the following specifications:

1. Number of clusters set to 3.
2. Dataset hard-coded into the algorithm.
3. Reads initial cluster centers from standard input.
4. Runs the k-means algorithm and halts when centers converge.
5. Computes the sum-of-squares error for the dataset with respect to the final cluster centers.

*Features*
1. Assigns each data point to the nearest cluster center.
2. Updates cluster centers based on the mean of assigned points.
3. Removes empty clusters after updates.
4. Outputs the sum-of-squares error rounded to 4 decimal places.
