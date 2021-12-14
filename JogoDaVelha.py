from GerenciadorPalavras import *
import io

temas = temasDisponiveis()

print('Os temas disponíveis são:')

[print(i, '- ', temas[i]) for i in range(len(temas))]

escolha = int(input('Digite sua escolha:\n'))

palavra = sortearPalavra(temas[escolha])
print(palavra)

palavraOculta = ['_ ' for _ in range(len(palavra))]


while True:
    letra = input('letra:\n')
    letraPos = -1


    while True:
        letraPos= palavra.find(letra, letraPos+1)
        print(letraPos)

        if(letraPos == -1):
            break

        palavraOculta[letraPos] = letra



    [print(i, end = '') for i in palavraOculta]
    print('\n')
