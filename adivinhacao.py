import random

print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randint(1,100)



chute = 1
while (chute <= 10) :
    num = int(input('Digite o Seu Chute: '))

    if (num == numero_secreto):
        print('Você Acertou!!!')
        chute = 11

    elif (num > numero_secreto):
        print("O Número digitado é maior que o número Secreto!")
        print('Tente Novamente')
        chute = chute + 1

    elif (num < numero_secreto):
        print('O número digitado é menor que o número secreto!')
        print('Tente Novamente')
        chute = chute +1

print('Jogo Finalizado!!!')