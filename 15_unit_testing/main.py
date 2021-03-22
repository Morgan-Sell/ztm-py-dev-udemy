def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        else:
            return "Please enter number"
    except ValueError as err:
       # returns an instance of the ValueError class.
       return err

