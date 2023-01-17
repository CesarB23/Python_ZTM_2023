#Usefull to asign values to variables as part of a larger expression
text = "hello0000054545"

if(n:= len(text)) > 10:
    print(f"Too long {n} characters")

while((n := len(text)) > 1):
    print(n)
    text = text[:-1]
print(text)