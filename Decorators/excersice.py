# Create an @authenticated decorator that only allows the 
# function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated2(fn):
    def wrapper(*args,**kwargs):
        #This solution doesnt works for many users, thats wrong
        if user1['valid']:
            return fn(*args,**kwargs)
    return wrapper
    

@authenticated2
def message_friends2(user):
    print('message has been sent')

message_friends2(user1)

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}
user2 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args,**kwargs):
        if args[0]['valid']:
            return fn(*args,**kwargs)
    return wrapper
    

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
message_friends(user2)
