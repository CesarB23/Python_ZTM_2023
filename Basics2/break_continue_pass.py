#Break ends the program in the line we indicate the program
i = 0
while i < 50:
    print(i)
    i += 1
    break
#Continue ignores the next lines and returns to the top of the loop
i = 0
while i < 50:
    continue
    print(i)
    i += 1
#Pass does nothing exactly but is usefull as a place holder while we are developing
for i in range(10):
    pass
