import random 

print("Super jogo da advinhação do número mágico!!")
numero_magico = random.randint(1,100)
numero_adivinhação = int(input("Escolha um número entre 1 e 100: "))
tentativas = 0

while numero_adivinhação != numero_magico:

    if numero_adivinhação > numero_magico:
        print("O número é menor. ")
    else:
        print("O número é maior. ")
    tentativas += 1 
    numero_adivinhação = int(input(" tente novamente: "))

print(f"Parabéns você acertou em {tentativas} tentativas !!")