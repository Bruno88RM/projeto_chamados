-- Criando a tabela de Clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT ,
    nome VARCHAR (100) NOT NULL ,
    email VARCHAR (100) UNIQUE NOT NULL ,
    telefone VARCHAR (20) ,
    cidade VARCHAR (50) ,
);
 --Criando a tabela de Chamados
 CREATE TABLE chamados (
    id_chamado INT PRIMARY KEY  AUTO_INCREMENT ,
    prioridade VARCHAR(20) ,
    setor VARCHAR (50) ,
    assunto VARCHAR (100)  NOT NULL,
    descricao TEXT ,
    status_chamado VARCHAR (20) DEFAULT 'aberto' ,
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP ,
    id_cliente  INT ,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)


 );