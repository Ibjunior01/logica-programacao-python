def login():
    username = "admin"
    password = "password123"
    tentativas = 3

    while tentativas > 0:
        user_input = input("Digite o nome de usuário: ")
        pass_input = input("Digite a senha: ")

        if user_input == username and pass_input == password:
            print("Bem-vindo(a) ao sistema!!! ")
            break

        tentativas -= 1
        print(f"Credenciais inválidas. Voce tem {tentativas} tentativas restantes.")

    if tentativas == 0:
        for _ in range(3):
            print("Acesso bloqueado!")
    
login()
