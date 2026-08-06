from database.conexao import inicializar_banco

def main():
    print("--- INICIANDO SISTEMA DE CHAMADOS TI ---")
    
    # Prepara o banco de dados ao iniciar o sistema
    inicializar_banco()

if __name__ == "__main__":
    main()