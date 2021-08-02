i = input('Olá, fale comigo,digite seu nome: ')
print('Prazer em conhecer, {}!'.format(i))
p = float(input('Me diga seu peso: '))
if p > 50:
    print('{:.0f} tá gordo hein {}!!!'.format(p, i))
else:
    print('{:.0f} tá magro hein {}!'.format(p, i))
print('Você é {}, e pesa {:.0f}!!'.format(i, p))
