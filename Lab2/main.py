import copy
from helper import *

n = 0
representation = []


def permute(size, lista):
    if size == 1:
        return lista
    else:
        return [
            y + x
            for y in permute(1, lista)
            for x in permute(size - 1, lista)
        ]


def backtracking():
    global n, representation
    visited = [copy.deepcopy(representation)]
    stack = [0]
    print(stack)
    while not should_stop(representation):
        added_to_stack = False
        for i in range(2 * n):
            for j in range(-1, 2 * n):
                new_representation = transition(copy.deepcopy(representation), i, j, n)
                if new_representation not in visited and new_representation != representation:
                    stack.append([i, j])
                    visited.append(copy.deepcopy(new_representation))
                    added_to_stack = True
                    representation = new_representation
                    break
            if added_to_stack:
                break
        if not added_to_stack:
            transition(representation, stack[-1][0], stack[-1][1], n)
            stack.pop()
            if len(stack) == 0:
                print('No solution can be found')
                return None
    stack.pop(0)
    print_solution(stack, n)


def run():
    global representation
    permutations = permute(2, list(map(str, range(n))))
    position = 0

    while not should_stop(representation):
        transition(representation, int(permutations[position][0]), int(permutations[position][1]), n)
        position = (position + 1) % len(permutations)


def main():
    global n, representation
    n = int(input('Number of pairs:'))
    representation = initialize(n)
    print(representation)
    # run()
    backtracking()


if __name__ == '__main__':
    main()
