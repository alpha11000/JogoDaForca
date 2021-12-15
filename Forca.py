partes = ['0', '/', '|', '\\', '/', '\\']

def desenharForca(erros):
    partesAtuais = ['' for _ in range(len(partes))]
    
    [partesAtuais.__setitem__(i, partes[i]) for i in range(erros)]
    print(partesAtuais)

    desenhoForca = ''
    desenhoForca += '_____\n'
    desenhoForca += '|    |\n'
    desenhoForca += '|    ' + partesAtuais[0] + '\n'
    desenhoForca += '|   ' + partesAtuais[1] + partesAtuais[2] + partesAtuais[3] + '\n'
    desenhoForca += '|   ' + partesAtuais[4] + ' ' + partesAtuais[5] + '\n'


    return desenhoForca
