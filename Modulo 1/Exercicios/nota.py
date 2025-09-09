nome = input("Digite o nome do aluno: ")
nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print(" Aprovado!")
elif media > 4:
    print("Recuperação")
else:
    print("Reprovado!")