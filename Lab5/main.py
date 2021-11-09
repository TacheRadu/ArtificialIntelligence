from minimax import *

def init():
    n = input("Input the number of colors: ")
    k = input("Input the sequence length: ")
    m = input("Input the maximum number of duplicates: ")
    initial_state = {"n": int(n), "k": int(k), "m": int(m), "colors": [-1] * int(k), "corrects": 0, "prev_states": []}
    return initial_state


# guess = list(map(int, input("Input your guess: ").split()))


def main():
    mode = input("Input the mode(1 for auto, 2 for manual): ")
    initial_state = init()
    if mode == "1":
        sequence = generate_colors(initial_state["n"], initial_state["k"], initial_state["m"])
    else:
        sequence = list(map(int, input("Input the sequence: ").split()))
        
    if len(sequence) != initial_state["k"]:
        print("Wrong sequence length")
        return
        
    for elem in sequence:
        if sequence.count(elem) > initial_state["m"]:
            print("Too many duplicates")
            return
            
    for elem in sequence:
        if elem < 0 or elem >= initial_state["n"]:
            print("Wrong color")
            return
        
    print(sequence)
        
    for i in range(initial_state["n"] * 2):
        guess = list(map(int, input("Input your guess: ").split()))
        if len(guess) != initial_state["k"]:
            print("Wrong sequence length")
            return
            
        for elem in guess:
            if guess.count(elem) > initial_state["m"]:
                print("Too many duplicates")
                return
            
        for elem in guess:
            if elem < 0 or elem >= initial_state["n"]:
                print("Wrong color")
                return
            
        correct_positions, correct_colors = check_sequence(sequence, guess)
        print("Correct positions: {}, correct colors: {}".format(correct_positions, correct_colors))
        initial_state["corrects"] = correct_positions
        initial_state["prev_states"].append({"corrects": initial_state["corrects"], "guess": guess})
        if correct_positions == initial_state["k"]:
            print("You won!")
            return
            
if __name__ == "__main__":
    #main()
    state = init()
    minimax(state['n'], state['k'], state['m'])
