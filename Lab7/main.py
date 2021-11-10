import numpy as np

EPOCS = int(input("How many epochs? "))
LR = float(input("Learning rate? "))

def sigmod(x):
    return 1/(1+np.exp(-x))