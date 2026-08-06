import sqlite3

def criar_conexao():
    """Cria e retorna uma conexão com o banco de dados."""
    return sqlite3.connect('sistema_ti.db')

def inicializar_banco():
    """Cria as tabelas necessárias no banco de dados se não existirem."""
    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prioridade TEXT DEFAULT 'BAIXA',
            status TEXT DEFAULT 'ABERTO',
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conexao.commit()
    conexao.close()
    print("[LOG] Banco de dados inicializado com sucesso!")