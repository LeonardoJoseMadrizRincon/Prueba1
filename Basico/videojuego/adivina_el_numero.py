import random as rd

def run():
    random_number = rd.randint(1,100)
    user_number = int(input('Ingrese un número entero entre el 1 y el 100: '))

    while random_number != user_number:
        if random_number > user_number:
            print('Elige un número más grande')
        elif random_number < user_number:
            print('Elige un número más pequeño')
        user_number = int(input("Elige otro número: "))

    print("Ganaste!!")


if __name__ == "__main__":
    run()
