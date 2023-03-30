print("Pressione a tecla enter para continuar...")
input()
username = input("Nome: ")
senha01 = "senha123"
num01 = 0
num02 = 3

while num01 < num02:
    senha02 = input("Senha: ")
    if senha02 == senha01:
        break
    else:
        print("Senha incorreta.")
        num01 += 1
if num01 == num02:
    print("Máxima tentativas de senha alcançada. Acesso negado.")
else:
    print("Acesso permitido. Bem-vindo, {}".format(username))