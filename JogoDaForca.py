from GerenciadorPalavras import *
from Forca import *
import os

temas = temasDisponiveis()

os.system('cls')
print('Os temas disponíveis são:')

[print(i, '- ', temas[i]) for i in range(len(temas))]

escolha = int(input('Digite sua escolha:\n'))

palavra = sortearPalavra(temas[escolha])


letrasEscolhidas = []
palavraOculta = ['_ ' for i in range(len(palavra))]
tentativasTotais = 6
tentativasRestantes = tentativasTotais

os.system('cls')

while True:
    erros = tentativasTotais - tentativasRestantes

    os.system('cls')
    print('Tema: ', temas[escolha])
    print('Letras usadas: ', ''.join(letrasEscolhidas))
    print(desenharForca(erros))
    print(''.join(palavraOculta))

    if(tentativasRestantes <= 0):
        print('Você perdeu :(')
        print('A palavra certa era: ', palavra)
        break

    letra = input('Digite uma letra: ')
    letraPos = -1
    letraCerta = False

    if(not letrasEscolhidas.__contains__(letra)):
        letrasEscolhidas += letra + ' '

    while True:
        letraPos= palavra.find(letra, letraPos+1)

        if(letraPos == -1):
            break

        letraCerta = True
        palavraOculta[letraPos] = letra

    if(not letraCerta):
        tentativasRestantes -= 1

    if(''.join(palavraOculta) == palavra):
        print('Você ganhou :D')
        break

