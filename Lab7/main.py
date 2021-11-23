import numpy as np
from numpy.core.fromnumeric import argmax

EPOCS = int(input("How many epochs? "))
LR = float(input("Learning rate? "))
HIDDEN_LAYER_SIZE = 69
f = open("dataset_and.txt", "r")
matrix = np.array(list(map(lambda x: int(x), f.read().split()))).reshape(4, 3)
labels = matrix[:, 2]
matrix = matrix[:, :2]


def sigmoid(x):
    return 1/(1+np.exp(-x))


def test(w_input, w_hidden, bias_input, bias_hidden):
    count = 0
    for j in range(4):
        x = matrix[j]
        z = sigmoid(np.dot(w_input, x) + bias_input)
        y = sigmoid(np.dot(w_hidden, z) + bias_hidden)
        if argmax(y) == labels[j]:
            count += 1
    
    return count/4


def train(matrix, epochs, learning_rate):
    w_input = np.random.normal(0, 1/2 ** 0.5, (HIDDEN_LAYER_SIZE, 2))
    #w_input = np.ones((HIDDEN_LAYER_SIZE, 2))
    bias_input = np.zeros(HIDDEN_LAYER_SIZE)
    w_hidden = np.random.normal(0, 1/HIDDEN_LAYER_SIZE ** 0.5, (2, HIDDEN_LAYER_SIZE))
    #w_hidden = np.ones((2, HIDDEN_LAYER_SIZE))
    bias_hidden = np.zeros(2)
    best = 0
    for i in range(epochs):
        for j in range(4):
            x = matrix[j]
            z = sigmoid(np.dot(w_input, x) + bias_input)
            y = sigmoid(np.dot(w_hidden, z) + bias_hidden)

            error_output = (y - [int(x == labels[j]) for x in range(2)]) * y * (1 - y)
            error_hidden = z * (1 - z) * np.dot(w_hidden.T, error_output)

            w_hidden -= learning_rate * np.outer(error_output.T, z)
            w_input -= learning_rate * np.outer(error_hidden.T, x)
            bias_hidden -= learning_rate * error_output
            bias_input -= learning_rate * error_hidden
        
        if test(w_input, w_hidden, bias_input, bias_hidden) > best:
            best = test(w_input, w_hidden, bias_input, bias_hidden)
            print("Best: {}".format(best))
    
    return w_input, w_hidden, bias_input, bias_hidden


if __name__ == '__main__':
    train(matrix, EPOCS, LR)
