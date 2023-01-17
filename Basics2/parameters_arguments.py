#Parameters are the inputs when we define the function
def say_hello(name='Borjalino',emoji='😄'):
    print(f'hello {name} {emoji}')
#Arguments are the actuall values we provide when we call the function
say_hello('Cesar','😀')

#Positional arguments are common way  a function takes as input
#If we modify the order of the input the function will do as well

#Keyword arguments helps to avoid typing or positional errors
say_hello(emoji='😀',name='Cesar')

#Also we can assing default parameters to the function
say_hello()
#Its usefull to call the function if actually is bad called