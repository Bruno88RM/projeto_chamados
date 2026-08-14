from database.conexao import inicializar_banco
from database.chamados import criar_chamado, listar_chamados

def main():
    print("--- INICIANDO SISTEMA DE CHAMADOS TI ---")
    
    # Prepara o banco de dados ao iniciar o sistema
    inicializar_banco()

    # Lista todos os chamados gravados
    listar_chamados()

if __name__ == "__main__":
    main()

    # Teste de inserção de um novo chamado
    # print("\n--- TESTANDO CRIAÇÃO DE CHAMADO ---")
    # criar_chamado(
    #     titulo="Impressora sem toner", 
    #     descricao="A impressora do RH parou de imprimir e pede substituição de toner.", 
    #     prioridade="Média"
    # )

if __name__ == "__main__":
    main()