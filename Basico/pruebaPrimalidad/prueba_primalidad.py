def check(number):
    dividers=0

    for i in range(1,number+1):
        if number%i == 0:
            dividers += 1

    if dividers>2 or dividers==1:
        salida1="No es primo"
    elif dividers == 2:
        salida1 = "Es primo"
    else:
        salida1 = "No se pudo concluir"

    return salida1


def run():
    number = int(input("Ingrese un número entero: "))
    salida2=check(number)
    print(salida2)

if __name__ == "__main__":
    run()
