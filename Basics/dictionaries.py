#Dictionary/ Hash table, unorderkey-value pair data structure/type
dictionary = {
    'a' : 1,
    'b' : 2
}
#Values in dicts are not right to each other as in lists/arrys
#Returns the value by indexing the key
print(dictionary['b'])
#We can use any data structure/type as a value of a dictionary
dictionary2 = {
    'a':123,
    'b':True,
    'c':[1,8,9],
    'd':'hello'
}
#But the keys must be an inmutable object