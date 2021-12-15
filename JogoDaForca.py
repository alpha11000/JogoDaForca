from GerenciadorPalavras import *
from Forca import *
import os

temas = temasDisponiveis()

os.system('cls')

print('Os temas disponíveis são:')

[print(i, '- ', temas[i]) for i in range(len(temas))]

escolha = int(input('Digite sua escolha:\n'))

palavra = sortearPalavra(temas[escolha])
#print(palavra)

#palavraOculta = [palavraOculta for _ in range(len(palavra))]
palavraOculta = ['_ ' for i in range(len(palavra))]
#palavraOculta = ''.join(palavraOcultaList)
print(palavraOculta)
tentativasTotais = 7
tentativasRestantes = tentativasTotais

os.system('cls')
print(''.join(palavraOculta))

while True:
    erros = tentativasTotais - tentativasRestantes
    print(desenharForca(erros))

    print('Tema: ', temas[escolha])
    print('tentativas = ', tentativasRestantes)
    letra = input('letra:\n')
    letraPos = -1
    letraCerta = False

    os.system('cls')

    while True:
        letraPos= palavra.find(letra, letraPos+1)

        if(letraPos == -1):
            break

        letraCerta = True
        palavraOculta[letraPos] = letra

    if(not letraCerta):
        tentativasRestantes -= 1
        print('Você errou')


    [print(i, end = '') for i in palavraOculta]
    print('\n')

    if(''.join(palavraOculta) == palavra):
        print('Você ganhou :D')
        break

    if(tentativasRestantes <= 0):
        print('Você perdeu :(')
        print('A palavra certa era: ', palavra)
        break
