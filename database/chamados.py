import sqlite3 
from database.conexao import criar_conexao


def criar_chamado(titulo, descricao, prioridade):
    """
    Insere um novo chamado na tabela 'chamados'.
    Prioridades sugeridas: 'Baixa', 'Média', 'Alta'
    """
    conn = criar_conexao()
    cursor = conn.cursor()

    # Query SQL para inserir o registro
    sql = """
    INSERT INTO chamados (titulo, descricao, prioridade)
    VALUES (?, ?, ?)
    """

    try:
        cursor.execute(sql, (titulo, descricao, prioridade))
        conn.commit()
        print(f"✅ [SUCESSO] Chamado '{titulo}' cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ [ERRO] Falha ao cadastrar chamado: {e}")
    finally:
        conn.close()

def listar_chamados():
    """
    Busca e exibe todos os chamados cadastrados no banco de dados.
    """
    conn = criar_conexao()
    cursor = conn.cursor()
    
    sql = "SELECT id, titulo, descricao, prioridade, status, data_criacao FROM chamados"
    
    try:
        cursor.execute(sql)
        chamados = cursor.fetchall()
        
        if not chamados:
            print("\n📭 Nenhum chamado encontrado.")
            return
            
        print("\n=== LISTA DE CHAMADOS ===")
        for c in chamados:
            print(f"ID: {c[0]} | Título: {c[1]} | Prioridade: {c[3]} | Status: {c[4]}")
            print(f"Descrição: {c[2]}")
            print(f"Data: {c[5]}")
            print("-" * 40)
            
    except sqlite3.Error as e:
        print(f"❌ [ERRO] Falha ao listar chamados: {e}")
    finally:
        conn.close()

def atualizar_status(id_chamado, novo_status):
    """Atualiza o status de um chamado pelo seu ID."""
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        # O UPDATE altera dados de linhas que já existem no banco
        sql = "UPDATE chamados SET status = ? WHERE id = ?"
        cursor.execute(sql, (novo_status, id_chamado))
        
        conn.commit()
        
        # cursor.rowcount nos diz quantas linhas foram modificadas
        if cursor.rowcount > 0:
            print(f"\n✅ [SUCESSO] Status do chamado ID {id_chamado} alterado para '{novo_status}'!")
        else:
            print(f"\n⚠️ [AVISO] Nenhum chamado foi encontrado com o ID {id_chamado}.")
            
    except Exception as e:
        print(f"\n❌ [ERRO] Falha ao atualizar o chamado: {e}")
    finally:
        conn.close()  

def deletar_chamado(id_chamado):
    """Exclui um chamado do banco de dados pelo seu ID."""
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        # O DELETE remove permanentemente a linha informada pelo ID
        sql = "DELETE FROM chamados WHERE id = ?"
        cursor.execute(sql, (id_chamado,))
        
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"\n🗑️ [SUCESSO] Chamado ID {id_chamado} removido do sistema!")
        else:
            print(f"\n⚠️ [AVISO] Nenhum chamado foi encontrado com o ID {id_chamado}.")
            
    except Exception as e:
        print(f"\n❌ [ERRO] Falha ao deletar o chamado: {e}")
    finally:
        conn.close()                      