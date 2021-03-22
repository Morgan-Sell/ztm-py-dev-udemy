 # File IO Errors

"""
NOTES:
-----

- Use FileNotFoundError to address errors.
- IOError occurs when the machine has problems reading, writing or performing another IO operation.

 """

try:
    with open('sad.txt', mode='X≈') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("File does not exist.")
    raise err
except IOError as err:
    print("IO error")
    raise err