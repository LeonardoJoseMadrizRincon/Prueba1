from functools import reduce

def run():
    my_list=[i for i in range(1,11)]
    odd=list(filter(lambda x: x%2==0,my_list))
    print("Probando la función filter")
    print(odd)

    my_list=[i for i in range(1,6)]
    squares=list(map(lambda i: i**2,my_list))
    print("\nProbando la función map")
    print(squares)
    
    my_list=[2,2,2,2,2]
    all_multiplied=reduce(lambda a,b: a*b, my_list)
    print("\nProbando la función reduce")
    print(all_multiplied)


if __name__ == "__main__":
    run()
