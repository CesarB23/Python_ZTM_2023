basket = ['a','b','x','d','c']
basket.sort()
basket.reverse()
print(basket[::-1]) # Using list slicing always creates a copy for instance
print(basket)
#A list of numbers with built in range function
print(list(range(100)))
#Join
    #Joining a list of items into a string example
new_sentence = ' '.join(['hi','my','name','is','Cesar'])
print(new_sentence)
#List unpacking
a,b,c = [1,2,3]
print(a,b,c)
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(type(a))
print(b)
print(c)
print(other)
print(type(other))
print(d)