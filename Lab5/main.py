import numpy as np
import random


def init():
    n = input("Input the number of colors: ")
    k = input("Input the sequence length: ")
    m = input("Input the maximum number of duplicates: ")
    initial_state = {"n": int(n), "k": int(k), "m": int(m), "colors": [-1] * int(k), "corrects": 0, "prev_states": []}
    return initial_state


def generate_colors(n, k, m):
    colors = [i for i in range(n) for j in range(m)]
    random.shuffle(colors)
    return colors[:k]


initial_state = init()
print(generate_colors(initial_state["n"], initial_state["k"], initial_state["m"]))
