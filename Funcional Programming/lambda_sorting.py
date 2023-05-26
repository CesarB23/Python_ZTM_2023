a = [(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x: x[1])
print(a)
print(sorted(a,key=lambda x: x[1]))