import random

print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
print("💥      jogo de adivinha    💥")
print("💥             do           💥")      
print("💥          fernando        💥")                          
print("💥       seja bem vindo     💥")
print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")

numeroSecreto = random.randrange(0, 100)
totalTentativas = 0
pontos = 100

print("Qual nível de dificuldade?")
print("(1) - Fácil (2) - Média (3) - Difícil")

nivel = int(input("Escolha um nível: "))

if nivel == 1:
    print("iiii não tá com nada frango 🤣")
    totalTentativas = 30
elif nivel == 2:
    print("eee tá melhor meu amigo 🫡👍")
    totalTentativas = 20
elif nivel == 3:
    print("você tá com coragem em 🫣🥶")
    totalTentativas = 10 
else:
    print("Nível inválido! O jogo será encerrado.")
    exit()

for rodada in range(1, totalTentativas + 1):
    print("Tentativa {} de {}".format(rodada, totalTentativas))
    chute_str = input("Digite um número entre 1 a 100: ")
    chute = int(chute_str)
    
    if chute < 1 or chute > 100:
        print("Número inválido")
        continue
    
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto
    
    if acertou:
        print(f"Você acertou e fez {pontos} pontos!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! Seu chute foi menor que o número secreto.")
            
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

    print("Fim de jodo ! 0 número era", numeroSecreto)



