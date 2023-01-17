#Set of unordere objects that are unique.
my_set = {1,2,3,4,5,6,7,8,9,9}
#Theres no duplicates in sets
print(my_set)
#We can convert lists into sets to avoid duplicates
my_list = [1,2,3,4,52,3,5,5]
print(set(my_list))
#Set methods
set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8,9,10}
    #Difference
print(set1.difference(set2))
    #Discard, kind of a pop method
set1.discard(7)
print(set1)
    #Difference_update
set1.difference_update(set2)
print(set1)
    #Intersection
set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8,9,10}
print(set1.intersection(set2))
print(set1 & set2)
    #Isdisjoint, sets have nothing in common
set1 = {1,2,3}
set2 = {4,5,6,7,8,9,10}
print(set1.isdisjoint(set2))
    #Union
print(set1.union(set2))
print(set1 | set2)
    #Issubset
set1 = {1,2,3}
set2 = {1,2,3,4,5,6,7,8,9,10}
print(set1.issubset(set2))
    #Issuperset
print(set2.issuperset(set1))