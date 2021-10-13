import random
import time
from random import randint

global n, representation


def initialize(n):
    return [[1 for i in range(n)], [1 for i in range(n)], 1]


def should_stop(representation):
    if sum(representation[0]) == 0 and sum(representation[1]) == 0 and representation[2] == 0:
        return True
    return False


def validate(state, husband, wife, who_gets_back):
    # who_gets_back == 0 -> husband gets back
    if representation[0][husband] != representation[1][wife]:
        return

    if who_gets_back == 1:
        state[0][husband] ^= 1
    else:
        state[1][wife] ^= 1

    if state[1][wife] != state[0][wife]:
        for i in range(n):
            if wife != i:
                if state[1][wife] == state[0][i] and state[1][i] != state[0][i]:
                    if who_gets_back == 1:
                        state[0][husband] ^= 1
                    else:
                        state[1][wife] ^= 1
                    return False
    return state


def transition(state: list, husband, wife, who_gets_back):
    global representation
    result = validate(state, husband, wife, who_gets_back)
    if result:
        print(result)
        representation = result


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

    while not should_stop(representation):
        transition(representation, int(permutations[position][0]), int(permutations[position][1]), randint(0,1))
        position = (position+1) % len(permutations)


def main():
    global n, representation
    n = int(input('Number of pairs:'))
    representation = initialize(n)
    run()


if __name__ == '__main__':
    main()
