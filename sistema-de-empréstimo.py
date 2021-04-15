"""
Sistema de idade para pegar empréstimo
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Não pode pegar o empréstimo')