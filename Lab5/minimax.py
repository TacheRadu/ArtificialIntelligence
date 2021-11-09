import random
import itertools


def generate_colors(n, k, m):
    colors = [i for i in range(n) for j in range(m)]
    random.shuffle(colors)
    return colors[:k]


def check_sequence(sequence, guess):
    correct_positions = 0
    for i in range(len(sequence)):
        if sequence[i] == guess[i]:
            correct_positions += 1

    correct_colors = 0
    for i in guess:
        if i in sequence:
            correct_colors += 1
    return correct_positions, correct_colors


def initial_guess(k: int, m: int) -> list[int]:
    step = (min(k, m) + 1) // 2
    return [i // step for i in range(k)]


def all_codes(n: int, k: int, m: int) -> set[list[int]]:
    code = [0] * k
    to_return = set()
    index = k - 1
    while True:
        index = k - 1
        while code[index] != n:
            to_return.add(code.copy())
            code[index] += 1
        if sum(code) == k * (n - 1) + 1:
            break
        while code[index] == n and index != 0:
            code[index] = 0
            index -= 1
            code[index] += 1
    real_return = to_return.copy()
    for x in to_return:
        for y in range(n):
            if x.count(y) > m:
                real_return.remove(x)
                break
    return real_return


def minimax(n: int, k: int, m: int):
    sequence = generate_colors(n, k, m)
    codes = all_codes(n, k, m)
    S = codes.copy()
    guess = initial_guess(k, m)
    while True:
        codes.remove(guess)
        correct_positions, correct_colors = check_sequence(sequence, guess)
        if correct_positions == k:
            print("Congrats.")
            break

        S = {x for x in S if check_sequence(guess, x)[0] != correct_positions
             and check_sequence(guess, x)[1] != correct_colors}


