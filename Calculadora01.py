num01 = float(input("Digite o número: "))
num02 = float(input("Digite outro número: "))

soma = (num01 + num02)
sub = (num01 - num02)
print(" soma ou subtração ?")
op = "soma"


if soma == op:
    print("Resultado: " ,soma)
else:
    print("Resultado: " ,sub)
