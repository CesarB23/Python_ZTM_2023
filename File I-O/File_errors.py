try:
    with open(r'C:\Users\52221\Desktop\Hola.txt',mode="r") as hola:
        print(hola.read())
except FileNotFoundError as err:
    print("File doesnt exist")
    print(err)
    # Prints the whole error 
    # raise err
