numero = None

while numero is None:
    try:
        numero = int(input('digite um numero int: '))
    except ValueError:
        print('erro:era pra ter digitado')

print(f'O numero digitado foi {numero}')