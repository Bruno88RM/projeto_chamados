# from database.conexao import inicializar_banco
# from database.chamados import criar_chamado, listar_chamados

# def main():
#     print("--- INICIANDO SISTEMA DE CHAMADOS TI ---")
    
#     # Prepara o banco de dados ao iniciar o sistema
#     inicializar_banco()

#     # Lista todos os chamados gravados
#     listar_chamados()

# if __name__ == "__main__":
#     main()

#     # Teste de inserção de um novo chamado
#     # print("\n--- TESTANDO CRIAÇÃO DE CHAMADO ---")
#     # criar_chamado(
#     #     titulo="Impressora sem toner", 
#     #     descricao="A impressora do RH parou de imprimir e pede substituição de toner.", 
#     #     prioridade="Média"
#     # )

# if __name__ == "__main__":
#     main()

from database.conexao import inicializar_banco
from database.chamados import (
    criar_chamado, 
    listar_chamados, 
    atualizar_status, 
    deletar_chamado
)

def exibir_menu():
    print("\n" + "="*35)
    print("      SISTEMA DE CHAMADOS TI      ")
    print("="*35)
    print("1 - Cadastrar Novo Chamado")
    print("2 - Listar Todos os Chamados")
    print("3 - Atualizar Status de um Chamado")
    print("4 - Excluir um Chamado")
    print("0 - Sair do Sistema")
    print("="*35)

def main():
    inicializar_banco()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-4): ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRO DE CHAMADO ---")
            titulo = input("Título do chamado: ")
            descricao = input("Descrição do problema: ")
            prioridade = input("Prioridade (Baixa / Média / Alta): ")
            
            criar_chamado(titulo, descricao, prioridade)
            
        elif opcao == "2":
            listar_chamados()
            
        elif opcao == "3":
            print("\n--- ATUALIZAR STATUS DE CHAMADO ---")
            listar_chamados()
            
            try:
                id_chamado = int(input("\nDigite o ID do chamado que deseja atualizar: "))
                
                print("\nOpções de Status:")
                print("1 - EM ANDAMENTO")
                print("2 - CONCLUÍDO")
                print("3 - CANCELADO")
                escolha_status = input("Escolha o novo status (1-3): ").strip()
                
                status_map = {
                    "1": "EM ANDAMENTO",
                    "2": "CONCLUÍDO",
                    "3": "CANCELADO"
                }
                
                if escolha_status in status_map:
                    novo_status = status_map[escolha_status]
                    atualizar_status(id_chamado, novo_status)
                else:
                    print("\n⚠️ Opção de status inválida!")
                    
            except ValueError:
                print("\n⚠️ Por favor, digite um número de ID válido.")

        elif opcao == "4":
            print("\n--- EXCLUIR CHAMADO ---")
            listar_chamados()
            
            try:
                id_chamado = int(input("\nDigite o ID do chamado que deseja EXCLUIR: "))
                
                # Trava de segurança para não apagar sem querer
                confirmacao = input(f"Tem certeza que deseja apagar o chamado ID {id_chamado}? (s/n): ").strip().lower()
                
                if confirmacao == 's':
                    deletar_chamado(id_chamado)
                else:
                    print("\nOperação cancelada!")
                    
            except ValueError:
                print("\n⚠️ Por favor, digite um número de ID válido.")
            
        elif opcao == "0":
            print("\nEncerrando o sistema... Até mais!")
            break
            
        else:
            print("\n⚠️ Opção inválida! Digite uma opção de 0 a 4.")

if __name__ == "__main__":
    main()