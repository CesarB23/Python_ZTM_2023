#An iterable is any Python object capable of returning its members one at a time
# ,permitting it to be iterated over in a for-loop.
#Iterated -> By one by one check each item in a collection
for letter in 'Hello':
    print(letter)
#Some functions that accept iterables as arguments are:
    #list,tuple,dict,set
    #sum,sorted,any,all,max,min
for i in [1,2,3,4,5]:
    print(i)
for i in (1,2,3,4,5):
    print(i)
for i in {1,2,3,4,5}:
    print(i)
#Dicts are a special case when we apply this same logic
#Python prints keys
user = {
    'name':'Golem',
    'age':5000,
    'powers':False
}

#Nested loops
for item in [1,2,3,4,5]:
    for x in ['a','b','c']:
        print(item,x)