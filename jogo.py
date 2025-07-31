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
    totalTentativas = 20
elif (nivel == 2):
    print(" eee ta melhor meu amigo 🫡👍")
    totalTentativas = 10
elif(nivel == 3):
    print(" voce ta com coram em 🫣🥶")
    totalTentativas = 30









