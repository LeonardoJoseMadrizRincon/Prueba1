# Crear, con dictionary comprehension, un diccioanrio cuyas llaves 
# sean los 1000 primeros números naturales con sus raíces cuadradas
# como valores

import math

def run():
    my_dict={i:math.sqrt(i) for i in range(1,1001)}

    for keys, value in my_dict.items():
        print(f"{keys}:{value}")

if __name__ == "__main__":
    run()
