




def check_guess(guess, answer):
    if 0 < int(guess) < 11:
        if guess == answer:
            return "you are a genius!"
        else:
            return "wrong answer. try again."
    else:
        return "Hey boludo, I said 1 to 10!"


def play_game(guess, answer):
    try:
        check_guess(guess, answer)
    
    except ValueError:
        return "please enter a number"
