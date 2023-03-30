#PRIMEIRA ATIVIDADE
num01 = float(input("Digite um número: "))

num02 = (num01 * 1.35)
num03 = (num01 * 1.15)

if num02 <= 300:
    print("Resultado: ",num02)
    print("35%")
else:
    print("Resultado " ,num03)
    print("15%")


#SEGUNDA ATIVIDADE
num01 = float(input("Digite o seu salário: "))

num02 = (num01 * 1.40)
num03 = (num01 * 1.50)
num04 = (num01 * 1.60)

if num02 >= 300 and num02 <= 1500:
    print("Seu salário será: " ,num02)
    print("40%")
if num03 >= 1500 and num03 <= 2500:
    print("Seu salário será: " ,num03)
    print("50%")
if num04 >= 2500 and num04 <= 5000:
    print("Seu salário será: " ,num04)
    print("60%")
else:
    print("Valores não se encaixam")

#Ou pode ser usado o comando "elif"
num01 = float(input("Digite o seu salário: "))

num02 = (num01 * 1.40)
num03 = (num01 * 1.50)
num04 = (num01 * 1.60)

if num02 >= 300 and num02 <= 1500:
    print("Seu salário será: " ,num02)
    print("40%")
elif num03 >= 1500 and num03 <= 2500:
    print("Seu salário será: " ,num03)
    print("50%")
elif num04 >= 2500 and num04 <= 5000:
    print("Seu salário será: " ,num04)
    print("60%")

else:
    print("Os valores não se encaixam.")

#TERCEIRA ATIVIDADE
num01 = int(input("Digite o número: "))
num02 = int(input("Digite outro número: "))
num03 = int(input("Digite o terceiro o número: "))

if num01 > num02 and num01 > num03:
    print("o número" ,num01, "é maior")

elif num02 > num01 and num01 > num03:
    print("O número" ,num02, "é maior")
    
else:
    print("o número" ,num03, "é maior")
    
#QUARTA ATIVIDADE
sigla = input("Digite a sigla do seu estado: ")

if sigla == "sp" or sigla == "rj":
    print("Você mora no sudeste")
elif sigla == "pb" or sigla == "pe":
    print("Você mora no nordeste")
    
else:
    print("Estado inválido.")

#QUINTA ATIVIDADE
num01 = int(input("Digite a sua idade: "))

if num01 >= 5 and num01 <=10:
    print("Infantil")
elif num01 >= 11 and num01 <= 17:
    print("Juventil")
elif num01 >= 18 and num01 <= 32:
    print("Adulto")
elif num01 >= 33 and num01 <= 99:
    print("Master")
    
else:
    print("Idade inválida.")