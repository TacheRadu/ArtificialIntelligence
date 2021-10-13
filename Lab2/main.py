import copy
from anytree import Node, RenderTree

n = 0
representation = []


def initialize_tree():
    global n
    tree = list()
    tree.append(Node(representation))


def initialize():
    return [[True for _ in range(n)], [True for _ in range(n)], True]


def should_stop():
    if True not in representation[0] and True not in representation[1] and representation[2] == False:
        return True
    return False


def validate(state: list, person_1: int, person_2: int) -> bool:
    global n
    # We have to move someone, and not the same person as two:
    if person_1 < 0 and person_2 < 0 or person_1 == person_2:
        return False

    # Check if those we want to move actually are on the side with the boat:
    if person_1 >= 0 and state[person_1 // n][person_1 % n] != state[2] or \
            person_2 >= 0 and state[person_2 // n][person_2 % n] != state[2]:
        return False

    # Simulate transition and check if condition holds:
    if person_1 >= 0:
        state[person_1 // n][person_1 % n] = not state[person_1 // n][person_1 % n]

    if person_2 >= 0:
        state[person_2 // n][person_2 % n] = not state[person_2 // n][person_2 % n]
    state[2] = not state[2]

    for i in range(n):
        if state[0][i] != state[1][i] and state[1][i] in state[0]:
            if person_1 >= 0:
                state[person_1 // n][person_1 % n] = not state[person_1 // n][person_1 % n]

            if person_2 >= 0:
                state[person_2 // n][person_2 % n] = not state[person_2 // n][person_2 % n]
            state[2] = not state[2]
            return False
    return True


def transition(state: list, person_1: int, person_2: int):
    validate(state, person_1, person_2)
    return state


def permute(size, lista):
    if size == 1:
        return lista
    else:
        return [
            y + x
            for y in permute(1, lista)
            for x in permute(size - 1, lista)
        ]


def print_solution(stack: list):
    representation = initialize()
    print(representation)
    for person_1, person_2 in stack:
        transition(representation, person_1, person_2)
        print(representation)


def backtracking():
    global n, representation
    visited = [copy.deepcopy(representation)]
    stack = [0]
    print(stack)
    while not should_stop():
        added_to_stack = False
        for i in range(2 * n):
            for j in range(-1, 2 * n):
                new_representation = transition(copy.deepcopy(representation), i, j)
                if new_representation not in visited and new_representation != representation:
                    stack.append([i, j])
                    visited.append(copy.deepcopy(new_representation))
                    added_to_stack = True
                    representation = new_representation
                    break
            if added_to_stack:
                break
        if not added_to_stack:
            transition(representation, stack[-1][0], stack[-1][1])
            stack.pop()
            if len(stack) == 0:
                print('No solution can be found')
                return None
    stack.pop(0)
    print_solution(stack)


def run():
    global representation
    permutations = permute(2, list(map(str, range(n))))
    position = 0

    while not should_stop():
        transition(representation, int(permutations[position][0]), int(permutations[position][1]))
        position = (position + 1) % len(permutations)


def main():
    global n, representation
    n = int(input('Number of pairs:'))
    representation = initialize()
    print(representation)
    # run()
    backtracking()


if __name__ == '__main__':
    main()
