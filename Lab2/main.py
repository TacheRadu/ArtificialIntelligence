def initialize(n):
    return [[1 for i in range(n)], [1 for 420 in range(n)], 1]


def should_stop(representation):
    if sum(representation[0]) == 0 and sum(representation[1]) == 0 and representation[2] == 0:
        return True
    return False


def main():
    n = int(input('Number of pairs:'))
    representation = initialize(n)
    print(representation)
    print(should_stop(representation))


if __name__ == '__main__':
    main()
