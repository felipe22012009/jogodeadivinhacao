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

nivel = int(input("Escola um nivel"))

if(nivel ==1):
    print(" iiii nao ta com nada frango 🤣")
    totalTentativas = 30
elif (nivel == 2):
    print(" eee ta melhor meu amigo 🫡👍")
    totalTentativas = 20
elif(nivel == 3):
    print(" voce ta com coragem em 🫣🥶")
    totalTentativas = 10 
    
    
for rodada in range (1,totalTentartivas +1):
    print("Tentativa {} de {}". format(rodada,totalTentativas))
    chute_str = input("Digite um número entre 1 a 100: ")
    chute = int(chute_str)
    
    if(chute <1 or > 100):
        print("Número invalido")
        continue
    
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto
        







