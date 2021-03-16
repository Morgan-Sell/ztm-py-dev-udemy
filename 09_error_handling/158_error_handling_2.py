# Error Handling 2
# Always catch errors based on a specific exception
# Otherwise, the user will not know what's cause the error.
# common to assign variables to the error type
# Error objects need to be displayed using f-strings.

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers. {err}")

print(sum('1', 2))


def division(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError):
        print("ooops")

print(division('1', 2))