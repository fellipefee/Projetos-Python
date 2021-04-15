
"""sistema de idade humana de um cachorro"""

idade = input('Digite a idade do seu cachorro: ')

#o sistema só aceitara numeros.
if idade.isdigit():
    idade = int(idade)

    if idade <= 1:
        print('Seu cachorro tem 15 anos humanos.')
    else:
        if idade <= 2:
            print('Seu cachorro tem 24 anos humanos.')
        elif idade <= 3:
            print('Seu cachorro tem 28 anos humanos.')
        elif idade <= 4:
            print('Seu cachorro tem 32 anos humanos.')
        elif idade <= 5:
            print('Seu cachorro tem 36 anos humanos.')
        else:
            pass
else:
    print("Por favor, digite um numero.")

