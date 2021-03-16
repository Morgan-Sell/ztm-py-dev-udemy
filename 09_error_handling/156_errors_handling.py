# Errors in Python
# Error handling allows the script to continue running if if errors exist.
# Example of errors: Key Error, Syntax Error
# Sometimes errors/exception are so severe that the program should terminate.
# Some of the most significant inputs occur when accepting inputs from users.

# ensure user submits an appropriate response to the age question
while True:
    try:
        age = int(input("What is your age? "))
        10 / age
    
    except ValueError:
        print('please enter a number')
        # STOPS the program
        raise Exception('Hey, cut it out!')
    
    except ZeroDivisionError:
        print('please enter age greater than 0')
        break

    # once an number is submitted
    else:
        print('thank you!')
        break

    # runs after everything has been executed
    # Is executed after "break", e.g. after the "else" statement
    finally:
        print("Ok, I am finally done!")