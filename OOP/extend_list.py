class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
print(len(super_list1))
lst = [1,2,3,4,5]
super_list1.append(lst)
print(super_list1)
print(lst[0])
print(issubclass(SuperList,list))