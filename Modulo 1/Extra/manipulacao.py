nome = input("Digite o nome do(a) aluno(a): ")
idade = int(input("Digite a idade do(a) aluno(a): "))


with open ("exemplo.txt", "a") as arquivo:
    arquivo.write(f"{nome} | {idade}\n")