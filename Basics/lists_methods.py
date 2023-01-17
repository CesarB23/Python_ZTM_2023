#Lists Methods.
basket = [1,2,3,4,5]
#Adding methods
    #Append
basket.append(6)
print(basket)
    #Insert
basket.insert(3,8)
print(basket)
    #Extend
basket.extend([10,11,12])
print(basket)
#Removing methods
    #Pop
basket.pop(0)
print(basket)
    #Remove
basket.remove(11)
print(basket)
    #Clear
basket.clear()
print(basket)
#Index methods
    #Index
basket = [1,2,3,4,5]
print(basket.index(3,0,3))
    #Reserved word "In" for searching items in a list,string, etc
print(8 in basket)
    #Count
print(basket.count(3))
    #Sort
basket = [8,1,2,9,0,5]
basket.sort()
print(basket)
    #Sorted, is a buit in function, no method
    #Dont modify the original list.
print(sorted(basket)) 
    #Copy
new_basket = basket.copy()
new_basket.append(15)
print(sorted(new_basket))
    #Reverse
basket.reverse()
print(basket)
