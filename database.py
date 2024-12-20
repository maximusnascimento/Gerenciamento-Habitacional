import pyodbc  
import os


def connect() -> str:
    try:
        global connection
        connection = pyodbc.connect(
            driver= # ex: SQL SERVER,
            server= # SERVIDOR,
            database= #,
            uid= # USUARIO,
            pwd= # SENHA
        )
    except Exception as e:
        return f"Erro ao conectar: {str(e)}"
    