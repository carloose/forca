import random

def jogar():
    print('JOGO DA FORCA')
    print('*************')
    sec = key()
    letSec = ['_' for _ in sec]

    erros = 0
    acertou = False
    enforcou = False
    print(letSec)

    while (not acertou and not enforcou):
        chute = input('Letra: ')
        if(chute in sec):
            pos = 0
            for i in sec:
                if (chute.upper() == i.upper()):
                    letSec[pos] = i
                pos += 1
        else:
            print('Letra incorreta!')
            erros +=1

        acertou = '_' not in letSec
        enforcou = erros == 6
        print(letSec)
        print('Erros: {}/6'.format(erros))

    if(acertou):
        print('Você acertou a palavra!\nPalavra: {}'.format(sec))
    elif(enforcou):
        print('Fim de jogo! x_x\nA palavra era: {}'.format(sec))

def key():
    sec = random.randint(4, 10)
    palavra = ''
    if sec == 4:
        palavra = 'lago'
    elif sec == 5:
        palavra = 'macho'
    elif sec == 6:
        palavra = 'lanche'
    elif sec == 7:
        palavra = 'cascata'
    elif sec == 8:
        palavra = 'biscoito'
    elif sec == 9:
        palavra = 'retificar'
    elif sec == 10:
        palavra = 'presunçoso'

    return palavra

jogar()




