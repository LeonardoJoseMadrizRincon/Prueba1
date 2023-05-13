# Crear con un list comprehension, una lista de todos los múltiplos de 4 que
# a la vez tambien son múltiplos de 6 y de , hasta 5 dígitos

def run():
    

    squares = [i for i in range(1,99999) if (i%4==0 and i%6==0 and i%9==0) and len(str(i))<5]
    print(squares)

if __name__ == "__main__":
    run()
