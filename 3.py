#vou dar um nome completo e quero separar os nomes

#split() #quebra em valores e passa em uma lista

#split(R) #posso dar parametro de separaçao


def separar_nome(nome_completo):
    lista = nome_completo.split()
    return lista[0],lista[1]

separar_nome('Renan Rodrigo')
##('Renan','Rodrigo') retorna em tupla
nome, sobrenome = separar_nome('Renan Rodrigo')
nome
##'Renan'
sobrenome
##'Rodrigo'

nome, sobrenome = separar_nome('Renan Rodrigo Alves')
##ele vai ignorar o 3 nome
# ******************************************************************
# Se vc não sabe qts argumentos ele vai passar  audio 01:34


def somar(*args):
        print(args)

somar()
##()

somar ### faltou completar
##########################################################################
def media(nome,*notas):
    total = 0
    for nota in notas:
            total += nota
    media = total / len(notas)
    return f'O aluno {nome} teve media{media}'