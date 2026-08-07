-- Povoando a tabela de clientes
INSERT INTO clientes(nome, email, telefone, cidade)
VALUES
('Bruno Ramon Marques','bruno@email.com','119999998888','São Paulo'),
('Maria Oliveira','maria@imail,com','119999998887', 'Santos');

--Povando a tabela de chamados
INSERT INTO chamados (descricao, id_cliente)
VALUES
('Erro ao acessar o sistema de login', 1),
('Solicitação de troca de senha', 2);