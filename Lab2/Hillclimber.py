from helper import *
import numpy as np

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
    person2 = np.random.randint(0, n*2)
    return person1, person2


def hillclimber():
    global n
    global representation
    while True:
        if should_stop(representation):
            print(representation)
            return
        this_value = heuristic(representation)
        new_representation = []
        while True:
            person1, person2 = generate_transition()
            if validate(representation, person1, person2, n):
                print("Swapping", person1, person2)
                new_representation = transition(representation, person1, person2, n)
                print(new_representation)
                break
        new_value = heuristic(new_representation)
        print(new_value)
        if(new_value < this_value):
            representation = new_representation



def main():
    global n
    global representation
    n = int(input("Enter the number of pairs: "))
    representation = initialize(n)
    print(representation)
    hillclimber()
    

if __name__ == "__main__":
    main()
