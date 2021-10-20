from consolemenu import *
from consolemenu.items import *
from BackTracking import *
from Hillclimber import *
from a_star import *


def permute(size, lista):
    if size == 1:
        return lista
    else:
        return [
            y + x
            for y in permute(1, lista)
            for x in permute(size - 1, lista)
        ]


def main():
    n = int(input('Number of pairs:'))
    representation = initialize(n)
    menu = ConsoleMenu('Husbands and wives problem', 'An artificial intelligence problem')
    do_backtracking = FunctionItem('BackTracking', backtracking, [representation])
    do_hillClimbing = FunctionItem('HillClimbing', hillclimber, [representation])
    do_a_star = FunctionItem('A*', a_star, [representation])
    menu.append_item(do_backtracking)
    menu.append_item(do_hillClimbing)
    menu.append_item(do_a_star)
    menu.show()


if __name__ == '__main__':
    main()
