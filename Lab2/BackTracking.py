import copy
from helper import *
def backtracking(representation):
    n = len(representation[0])
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


