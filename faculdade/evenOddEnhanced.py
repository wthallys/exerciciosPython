def evenOdd(x):
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        print(f"{x} -> ", end="")


evenOdd(13)