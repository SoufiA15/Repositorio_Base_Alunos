numero = int(input("Digite um número: "))
inicio = int(input("Digite o início: "))
final = int(input("Digite até onde deve ir: "))

for i in range(inicio,final + 1):
        print(f"{i} x {numero} = {i * numero}")
