peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)
print(imc)

if imc <= 18.5: 
    print("Abaixo do peso ")
elif imc <= 24.9:
    print("Peso normal ")
elif imc <= 29.9:
    print("Sobrepeso ")
elif imc <= 30:
    print("Cuidado com a saúde ")
elif imc <= 34.9:
    print("Obesidade grau I ")
elif imc <= 39.9:
    print("Obesidade grau II")

if imc >= 40:
    print("Obesidade de grau III, mórbida")

