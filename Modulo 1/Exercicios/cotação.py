COTACAO_DOLAR = 5 

def real_dolar(reais):
    return reais /COTACAO_DOLAR

def dolar_real(dolar):
    return dolar * COTACAO_DOLAR

opcao = input("Selecione a opçãoque deseja: \n" \
"[1 -> Converter de Real para Dolár]\n" \
"[2 -> Converter de Dolár para Real]")

if opcao == "1":
    real = float(input("Digite a quantidade de reais que você quer converter:  "))
    print(real_dolar(real))

else:
    dolar = float(input("Digite a quantidade de dolares que você quer converter: "))
    print(dolar_real(dolar))