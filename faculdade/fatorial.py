# num = int(input("Digite um numero inteiro:"))

# def fatorial(num):
#     if num == 1 or num == 0:
#         return 1
#     return num * fatorial(num - 1)

# print(f'Fatorial: {fatorial(num)}')

num = int(input("Digite um numero inteiro:"))

fatorial = 1
while (num > 1):
    fatorial = fatorial * num
    num -= 1
print()
print(f'Fatorial: {fatorial}')