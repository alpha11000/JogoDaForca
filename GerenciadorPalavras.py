from random import choice

nomeArquivo = 'Palavras/palavras.txt'

def temasDisponiveis():
    
    temas = []


    with open(nomeArquivo) as arquivo:

        texto = arquivo.read()
       
        temaStart = 0
        temaEnd = 0

        while True:

            temaStart = texto.find('#', temaEnd)
            temaEnd = texto.find('\n', temaStart)

            if temaStart == -1: 
                break

            if temaEnd == -1:
                tema = texto[temaStart + 1]
            else:
                tema = texto[temaStart + 1: temaEnd]

            temas.append(tema)

    return temas

def randomizarTema(temas = []):
    tema = choice(temas)
    return tema

def sortearPalavra(tema):
    
    palavras = []

    with open(nomeArquivo) as arquivo:

        texto = arquivo.read()

        startPalavras = texto.find('#' + tema)
        startPalavras = texto.find('\n', startPalavras)

        endPalavras = texto.find('#', startPalavras)

        textoPalavras = texto[startPalavras + 1: endPalavras - 1]
        palavras = textoPalavras.splitlines()
        
        return choice(palavras)
        
    