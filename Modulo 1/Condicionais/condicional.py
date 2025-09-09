print("-------------------------" )
print("SISTEMA DA BIBLIOTECA")
print("-------------------------" )
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
carteirinha = input("Possui a carteirinha da biblioteca? \n (1-Sim / 2- Não)")

if idade >= 18:
   if carteirinha == "1":
    print("Cadastro realizado com sucesso! ")
   else: 
    print("Você não pode se cadastrar: ")
else: 
  print("Requesito que seja maior de idade e tenha a carteirinha.")    