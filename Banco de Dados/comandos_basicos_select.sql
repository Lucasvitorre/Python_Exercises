-- Testando o código --
-- Selecionando algumas colunas da tabela pedidos. --
select 
	Data_Venda, 
    ID_Cliente, 
    ID_Pedido
from pedidos;

-- Selecionando todas as colunas da tabela pedidos. --
select * from pedidos;

-- Alterando nome "Apelido" na consulta das colunas --
select 
	ID_Cliente as "ID Cliente",
    Nome,
    Data_Nascimento as "Data de Nascimento ",
    Email
from clientes;
	
-- Utilizando o comando limit para as 5 primeiras linhas --

select * from produtos
limit 5 ;

-- Utilizando o comando limit para as 5 primeiras linhas, ordenando pelo o Preco_Unit--
select *  from produtos
order by Preco_Unit DESC;

