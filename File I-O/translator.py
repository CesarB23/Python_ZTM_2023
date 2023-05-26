from translate import Translator

translator= Translator(to_lang="pt")

with open('Texto.txt',mode='r') as txt:
    text = txt.read()
    translation = translator.translate(text) 
    print(translation)
    txt.close()  
    with open("Texto_traducido.txt",mode="w") as txt:
        txt.write(translation)
        txt.close()     


f = open("Texto.txt","r")
translation = translator.translate(f.read())
print(translation)
f =open("Texto_traducido_2.txt","w")
f.write(translation)
