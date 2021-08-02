idade = int(input('Informe sua idade: '))
if idade < 14:
    print('CRIANÇA')
elif idade < 18:
    print('Você ainda não pode dirigir!')
elif idade >= 60:
    print('Idoso')
else:
    print('Você é o cara!!!')
