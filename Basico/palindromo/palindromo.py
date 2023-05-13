def check(word):
    word=word.replace(' ','')
    word=word.lower()
    word=word.strip()

    if word==word[::-1]:
        salida1="Es un palíndromo"
    elif word!=word[::-1]:
        salida1="No es un palíndromo"
    else:
        salida1="No se pudo concluir...."
    return salida1

def run():
    palabra=input("Escribe una palabra: ")
    salida2=check(palabra)
    print(salida2)

if __name__ == "__main__":
    run()
