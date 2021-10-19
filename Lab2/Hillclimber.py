from numpy.lib.function_base import copy
from helper import *
import numpy as np
import copy

n = 0
representation = []


def heuristic(state):
    sum = 0
    for i in state[0]:
        sum += not i
    for i in state[1]:
        sum += not i
    return sum


def generate_transition():
    person1 = np.random.randint(0, n*2)
    person2 = np.random.randint(-1, n*2)
    return person1, person2


def hillclimber():
    global n
    global representation
    while True:
        if should_stop(representation):
            print(representation)
            return
        print(representation)
        old_representation = copy.deepcopy(representation)
        this_value = heuristic(representation)
        while True:
            person1, person2 = generate_transition()
            if validate(representation, person1, person2, n):
                transition(representation, person1, person2, n)
                print("Swapping", person1, person2)
                print(representation)
                break
        print(heuristic(representation), this_value)
        if(heuristic(representation) < this_value):
            representation = old_representation


def main():
    global n
    global representation
    n = int(input("Enter the number of pairs: "))
    representation = initialize(n)
    hillclimber()
    

if __name__ == "__main__":
    main()
