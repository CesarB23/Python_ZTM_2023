#What actually decorators do when we call it

def my_decorator(func):
    def wrap_func():
        print("*****")
        func()
        print("*****")
    return wrap_func

def hello():
    print("hello")

#Decorators take the function as input, takes place of the "func"
a = my_decorator(hello)
#a is returned as the wrap_func value
a()