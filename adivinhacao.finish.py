import random

print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randint(1,20)



chute = 1
while (chute <= 10) :
    num = int(input('Digite o Seu Chute: '))
    acertou = num == numero_secreto
    maior = num > numero_secreto
    menor = num < numero_secreto
    tentativa = ('Tente Novamente')

    if (acertou):
        print('Você Acertou!!!')
        chute = 11

    elif (maior):
        print("O Número digitado é maior que o número Secreto!")
        if (chute <= 9) :
            print(tentativa)
        chute = chute + 1

    elif (menor):
        print('O número digitado é menor que o número secreto!')
        if (chute <= 9):
            print(tentativa)
        chute = chute +1
if (chute == 11):
    print('Jogo Finalizado!!!')
else :
    print('O Número Secreto era: {}'.format(numero_secreto))
    print('Jogo Finalizado!!!')