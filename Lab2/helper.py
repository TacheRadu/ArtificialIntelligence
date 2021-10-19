def transition(state: list, person_1: int, person_2: int, n):
    validate(state, person_1, person_2, n)
    if person_1 < n:
        state[0][person_1] = not state[0][person_1]
    else:
        state[1][person_1 - n] = not state[1][person_1 - n]
    if person_2 < n:
        state[0][person_2] = not state[0][person_2]
    else:
        state[1][person_2 - n] = not state[1][person_2 - n]
    return state


def initialize(n):
    return [[True for _ in range(n)], [True for _ in range(n)], True]


def should_stop(representation):
    if True not in representation[0] and True not in representation[1]:
        return True
    return False


def validate(state: list, person_1: int, person_2: int, n) -> bool:
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