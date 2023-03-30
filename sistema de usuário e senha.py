print("Aperte a tecla enter para continuar...")
input()
username = input("Nome: ")
senha01 = "senha123"
senha02 = input("Senha: ")

while senha01 != senha02:
    print("Senha incorreta. Tente novamente.")
    senha02 = input("Senha: ")

print("Welcome," ,username)