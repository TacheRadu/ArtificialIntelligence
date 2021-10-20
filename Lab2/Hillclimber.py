from numpy.lib.function_base import copy
from helper import *
import numpy as np
import copy


def generate_transition(n):
    person1 = np.random.randint(0, n*2)
    person2 = np.random.randint(-1, n*2)
    return person1, person2


def hillclimber(representation):
    n = len(representation[0])
    while True:
        if should_stop(representation):
            print(representation)
            return
        print(representation)
        old_representation = copy.deepcopy(representation)
        this_value = heuristic(representation)
        while True:
            person1, person2 = generate_transition(n)
            if validate(representation, person1, person2, n):
                transition(representation, person1, person2, n)
                print("Swapping", person1, person2)
                print(representation)
                break
        print(heuristic(representation), this_value)
        if heuristic(representation) < this_value:
            representation = old_representation


def main():
    n = int(input("Enter the number of pairs: "))
    representation = initialize(n)
    hillclimber(representation)
    

if __name__ == "__main__":
    main()
