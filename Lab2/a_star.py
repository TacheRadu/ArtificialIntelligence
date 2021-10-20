import copy

from helper import *


def best_open(open_list: list):
    if len(open_list) == 0:
        return -1
    min_cost = heuristic(open_list[0])
    res = open_list[0]
    for i in range(len(open_list)):
        a = heuristic(open_list[i])
        if a < min_cost:
            min_cost = a
            res = open_list[i]
    return res


def get_valid_neighbours(state: list):
    res = []
    for i in range(len(state[0]) * 2):
        for j in range(-1, len(state[0]) * 2):
            if validate(state, i, j, len(state[0])):
                transition(state, i, j, len(state[0]))
                res.append(copy.deepcopy(state))
                transition(state, i, j, len(state[0]))
    return res


def a_star(representation: list):
    path = []
    open_list = [representation]
    closed_list = []
    while len(open_list):
        q = best_open(open_list)
        path.append(q)
        open_list.remove(q)
        neighbours = get_valid_neighbours(q)
        for neighbour in neighbours:
            if should_stop(neighbour):
                path.append(neighbour)
                for node in path:
                    print(node)
                return None
            if neighbour not in open_list and neighbour not in closed_list:
                open_list.append(neighbour)
        closed_list.append(q)
    print('No solution could be found')


def main():
    n = int(input("Enter the number of pairs: "))
    representation = initialize(n)
    a_star(representation)


if __name__ == '__main__':
    main()