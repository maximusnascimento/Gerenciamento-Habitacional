import pyodbc

def connect() -> str:
    try:
        connection = pyodbc.connect(
            driver='{SQL Server}',
            server='SEU_SERVIDOR', 
            database='SEU_BANCO',  
            uid='SEU_USUARIO',     
            pwd='SUA_SENHA'        
        )
        return "Conexão estabelecida com sucesso!"
    except:
        return "Erro ao conectar"
