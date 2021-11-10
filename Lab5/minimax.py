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
    return correct_positions, correct_colors - correct_positions


def initial_guess(k: int, m: int) -> tuple[int]:
    step = (min(k, m) + 1) // 2
    return tuple([i // step for i in range(k)])

def all_codes(n: int, k: int, m: int) -> list[tuple[int]]:
    code = [0] * k
    to_return = list()
    index = k - 1
    while True:
        index = k - 1
        while code[index] != n:
            to_return.append(tuple(code.copy()))
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


def generate_pegs(k: int) -> set[tuple[int]]:
    s = set()
    for i in range(k + 1):
        for j in range(k + 1 - i):
            s.add((i,j))
    return s


def mini(codes: list[tuple[int]], pegs: set[tuple[int]], S: list[tuple[int]]) -> dict[tuple[int], int]:
    to_return = dict()
    for code in codes:
        to_return[code] = min([len([x for x in S if check_sequence(code, x) != peg]) for peg in pegs])
    return to_return


def maxi(minis: dict[tuple[int], int]) -> list[tuple[int]]:
    return [x for x in minis.keys() if minis[x] == max(minis.values())]
    

def minimax(n: int, k: int, m: int):
    sequence = generate_colors(n, k, m)
    codes = all_codes(n, k, m)
    S = codes.copy()
    guess = initial_guess(k, m)
    pegs = generate_pegs(k)
    count = 0
    while True:
        count += 1
        codes.remove(guess)
        correct_positions, correct_colors = check_sequence(sequence, guess)
        if correct_positions == k:
            print("Congrats.")
            print(count)
            break

        S = [x for x in S if check_sequence(guess, x) == (correct_positions, correct_colors)]
        candidates = maxi(mini(codes, pegs, S))
        candidates_in_S = [x for x in candidates if x in S]
        if len(candidates_in_S) != 0:
            guess = random.choice(candidates_in_S)
        else:
            guess = random.choice(candidates)
        



