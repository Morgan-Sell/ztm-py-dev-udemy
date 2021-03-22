import sys
from random import randint


start_num = int(sys.argv[1])
end_num = int(sys.argv[2])

answer = randint(start_num, end_num)

while True:
    try:
        guess = int(input(f"Guess an integer between {start_num} and {end_num}, inclusive --> "))
        if start_num <= guess <= end_num:
            if guess == answer:
                print("Great job! Eres un genio!!")
                break
        else:
            print("Choose a number within the range")

    except ValueError:
        print("Choose an integer, boludo!")



