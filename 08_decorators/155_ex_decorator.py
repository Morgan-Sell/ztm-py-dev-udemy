# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

# args is a tuple that contains all the arguments passed to the function.
# args[0] is the first item in the tuple.
# In this example, args[0] is a dictionary.
def authenticated(fn):
  # code here
    def wrap_func(*args, **kwargs):
        # args[0]
        is_auth = args[0]['valid']
        if is_auth:
            return fn(*args, **kwargs)
    return wrap_func

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)