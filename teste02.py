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