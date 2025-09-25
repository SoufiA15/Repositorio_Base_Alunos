def calcular_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

valor_hora = float(input("Digite quanto você ganha por hora: "))
hora = float(input("Digite o números de horas trabalhadas no mês: "))

salario = calcular_salario(hora, valor_hora)

print(f"Seu salário do mês é: {salario:.2f}")