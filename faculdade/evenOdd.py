def evenOdd(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1
        # return evenOdd(3 * x + 1)

print(evenOdd(13))