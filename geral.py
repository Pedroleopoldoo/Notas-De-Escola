# Repetição (vários alunos)
from time import sleep
from matplotlib import pyplot as plt

a = []
media = []
print('Sistema de notas geral')

for c in range(1, 5):
    for n in range(1, 3):
        perg = float(input(f'Qual a sua {n}º nota do {c}º semestre? '))
        a.append(perg)
    media.append((a[0] + a[1]) / 2)
    a.clear()
    sleep(2)
    if media[c - 1] >= 7:
        print(f'Média positiva no {c}º semestre de {media[c - 1]}')
        sleep(2)
    elif 0 <= media[c - 1] < 7:
        print('Recuperação')
        rec = float(input('Coloque a nota da recuperação: '))
        sleep(2)
        if (media[c - 1] + rec) / 2 >= 7:
            media.append((media[c - 1] + rec) / 2)
            media.pop(c - 1)
            print(f'Recuperação deixou sua média positiva no {c}º semestre com a média {media[c - 1]}')
            sleep(2)
        elif 0 <= (media[c - 1] + rec) / 2 < 7:
            print('Sua média continua baixa, estude mais', end=', ')
            if rec > media[c - 1]:
                media.append((media[c - 1] + rec) / 2)
                media.pop(c - 1)
                print(f'sendo ela {media[c - 1]}')
                sleep(2)
            else:
                print(f'sendo ela {media[c - 1]}')
                sleep(2)
        else:
            print('ERRO')
    else:
        print('ERRO')

medfinal = (media[0] + media[1] + media[2] + media[3]) / 4
if medfinal >= 7:
    print('Meus parabéns, você passou de ano!!')
elif 0 <= medfinal < 7:
    print('Você está de recuperação final')
    rec = float(input('Coloque a sua nota recuperação final: '))
    sleep(2)
    if (medfinal + rec) / 2 >= 7:
        print('Meus parabéns, você passou de ano')
    else:
        print('Você repetiu de ano, estude mais ano que vem')
else:
    print('ERRO!!')

gra = str(input('Você deseja mostrar um gráfico de desempenho? [S/N] ')).upper()
if gra == 'S':
    x = list(range(1, 5))
    y = media
    plt.plot(x, y, marker='o')
    plt.title('Média geral')
    plt.xlabel('Provas')
    plt.ylabel('Notas')
    plt.show()
else:
    print('Tenha um ótimo dia!!')
