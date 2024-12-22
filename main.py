import database

# Menu principal
def main():
    print("===================================")
    print("+           Bem Vindos,           +")
    print("+    Gerenciamento Habitacional   +")
    print("===================================")
    
    print(database.connect())  

    while True:
        print("\nMenu Principal")
        print("[1] Cadastro de Usuários")
        print("[2] Login")
        print("[3] Cadastro de Imóveis")
        print("[4] Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                database.cadastro()  
            elif opcao == 2:
                pass
            elif opcao == 3:
                database.cadastroImoveis()  
            elif opcao == 4:
                print("Encerrando o programa...")
                database.connection.close()  
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()