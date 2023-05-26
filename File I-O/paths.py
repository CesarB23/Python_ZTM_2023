#Absolute file path, use r to give path in windows
with open(r'C:\Users\52221\Desktop\Arduino\Hola.txt',mode="r") as hola:
    print(hola.read())