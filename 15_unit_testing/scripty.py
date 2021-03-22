




def check_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("you are a genius!")
            break
    else:
        print("Hey boludo, I said 1 to 10!")


def play_game(guess, answer):
    try:
        check_guess(guess, answer)
    
    except ValueError:
        print("please enter a number")
