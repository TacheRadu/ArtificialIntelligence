n = 0
representation = []


def initialize():
    return [[1 for _ in range(n)], [1 for _ in range(n)], 1]


def should_stop():
    if sum(representation[0]) == 0 and sum(representation[1]) == 0 and representation[2] == 0:
        return True
    return False


def validate(state: list, person_1: int, person_2: int) -> bool:
    global n
    # We have to move someone:
    if person_1 < 0 and person_2 < 0:
        return False

    # Check if those we want to move actually are on the side with the boat:
    if person_1 >= 0 and state[person_1 // n][person_1 % n] != state[2] or \
            person_2 >= 0 and state[person_2 // n][person_2 % n] != state[2]:
        return False

    # Simulate transition and check if condition holds:
    state[person_1 // n][person_1 % n] = not state[person_1 // n][person_1 % n]
    state[person_2 // n][person_2 % n] = not state[person_2 // n][person_2 % n]
    for i in range(n):
        if state[0][i] != state[1][i] and state[1][i] in state[0]:
            return False
    return True


def transition(state: list, person_1: int, person_2: int):
    if validate(state, person_1, person_2):
        state[person_1 // n][person_1 % n] = not state[person_1 // n][person_1 % n]
        state[person_2 // n][person_2 % n] = not state[person_2 // n][person_2 % n]
        state[2] = not state[2]

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


if __name__ == '__main__':
    main()
