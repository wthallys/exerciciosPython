"""
Programa iniciamente sem nome, mas, que depois de testes foi nomeado
assim: "Amostra do vem por aí!"
"""
name = input("Hi, my name is Pyt. what's your name? ")
v2 = name.isnumeric()
if v2 == False:
    print('Nice to meet you {}!'.format(name))
    v3 = input('Do you like know a curiosity about me?(yes or no) ')
    while v3 != 'yes' and v3 != 'no':
        print('=====yes or no=====')
        v3 = input('Do you like know a curiosity about me? ')
    if (v3 == 'yes'):
        print("lets go!\nI'm being developed by a beginner programmer!")
        print("I'm being test fase.")
    elif (v3 == 'no'):
        print('Ok, later.')
    else:
        print('Error!')
else: 
    print('Error!! Restart the program!!')
