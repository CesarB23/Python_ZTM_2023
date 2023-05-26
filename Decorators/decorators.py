#Decorators allow functions to act like variables, first class citizens
#Add extra features to it
#Notation: @something

# @class
def hellou():
    pass

#Higher Order Function
    #Functions that recieves other functions as inputs
    #Functions that return another functions

#Higher order func
def my_decorator(func):
    def wrap_func():
        print("*****")
        func()
        print("*****")
    return wrap_func

@my_decorator
def hello():
    print("hello")

hello()