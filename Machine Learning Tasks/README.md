This repository contains two Tasks for the Adaptive Computation and Machine Learning (ACML) Module. Each task is implemented in Python and is described below.

**Task 1: Implementing a Neural Network**

*Description:* 

This Task involves creating a Python program that implements a neural network with the following specifications:

- Input layer with 4 nodes
- Hidden layer with 8 nodes
- Output layer with 3 nodes
- Sigmoid activation function for hidden and output layers
- Weights and biases initialized to 1

*Features*

- Feedforward step to compute the network's output for given inputs.
- Sum-of-squares loss computation between the network's output and target values.
- Backpropagation method for updating weights and biases with a learning rate of 0.1.

**Task 2: Implementing the k-means Algorithm**

*Description:* 

This Task involves creating a Python program that implements the k-means algorithm with the following specifications:

- Number of clusters set to 3.
- Dataset hard-coded into the algorithm.
- Reads initial cluster centers from standard input.
- Runs the k-means algorithm and halts when centers converge.
- Computes the sum-of-squares error for the dataset with respect to the final cluster centers.

*Features*

- Assigns each data point to the nearest cluster center.
- Updates cluster centers based on the mean of assigned points.
- Removes empty clusters after updates.
- Outputs the sum-of-squares error rounded to 4 decimal places.
