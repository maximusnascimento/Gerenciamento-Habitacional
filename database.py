import pyodbc 

def connect() -> str:
    try:
        global connection
        connection = pyodbc.connect(
            driver='{SQL Server}',
            server='SEU_SERVIDOR', 
            database='SEU_BANCO',  
            uid='SEU_USUARIO',     
            pwd='SUA_SENHA'   
        )
        return "Conexão estabelecida com sucesso."
    except Exception as e:
        return f"Erro ao conectar: {str(e)}"


def cadastro():
    cursor = connection.cursor()
    print("CADASTRO DE USUÁRIOS")
    try:
        nome = input("Digite o seu nome para cadastro: ")
        while True:
            email = input("Digite o seu email para cadastro: ")
            if "@" not in email:
                print("Não é um email válido. Por favor, tente novamente.")
            else:
                break
        senha = input("Digite uma senha para cadastro: ")

        command = """
        INSERT INTO ip.usuarios (nome, email, senha)
        VALUES (?, ?, ?)
        """
        cursor.execute(command, (nome, email, senha))
        connection.commit()
        print("\nCadastro realizado com sucesso.")
    except Exception as e:
        print(f"Erro ao realizar o cadastro: {str(e)}")

def cadastroImoveis():
    cursor = connection.cursor()
    print("\nCadastro de imóveis\n")
    try:
        enderecoImovel = input("Digite o endereço para cadastrar: ")
        while True:
            print("[1] Casa")
            print("[2] Apartamento")
            op = int(input("Escolha uma das opções de imóvel: "))
            if op == 1 or op == 2:
                tipoImovel = "Casa" if op == 1 else "Apartamento"
                print("Tipo de imóvel escolhido -", tipoImovel)
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        tamanhoImovel = int(input("Digite o tamanho do imóvel (em m²): "))
        if tamanhoImovel <= 0:
            raise ValueError("Tamanho do imóvel inválido.")

        valorImovel = float(input("Digite o valor do imóvel (em R$): "))
        if valorImovel <= 0:
            raise ValueError("Valor do imóvel inválido.")

        command = """
        INSERT INTO ip.imoveis (endereco, tipo, tamanho, valor)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(command, (enderecoImovel, tipoImovel, tamanhoImovel, valorImovel))
        connection.commit()
        print("\nImóvel cadastrado com sucesso.")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Erro ao realizar o cadastro do imóvel: {str(e)}")

def login():
    cursor = connection.cursor()
    print("LOGIN")
    try:
        while True:
            email = input("Digite o seu email para login: ")
            if "@" not in email:
                print("Não é um email válido. Por favor, tente novamente.")
            else:
                break

        senha = input("Digite a senha para login: ")

        command = "SELECT * FROM ip.usuarios WHERE email = ? AND senha = ?"
        cursor.execute(command, (email, senha))
        result = cursor.fetchone() 

        if result:
            print("Login bem-sucedido!")
            return True 
        else:
            print("Usuário inválido")
            return False  
    except Exception as e:
        print(f"Erro no login: {e}")
        return False 
    finally:
        cursor.close()

