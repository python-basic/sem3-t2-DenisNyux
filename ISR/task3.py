def fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fib(x-1)+fib(x-2)


def main():
    print(fib(10))


main()