-- Exemplo 1, Utilize o GROUP BY para criar
-- uma consulta e descobrir o total de clientes por sexo.

SELECT
    Sexo,
    COUNT(*) AS "Qtd. Clientes"
FROM clientes
GROUP BY Sexo;

-- Exemplo 2, faça uma consulta à tabela de produtos para retornar
-- o total de produtos por marca.
SELECT
    Marca_Produto,
    Count(*) AS "Qts. de Produtos"
From produtos
GROUP BY Marca_Produto;

-- Exemplo 3, Faça uma consulta à tabela Pedidos e descubra
-- a Receita Total e Custo Total por ID_Loja.

SELECT
    ID_Loja,
    SUM (Receita_venda) AS "Receita Total",
    SUM (Custo_Venda)  AS "Custo Total"
FROM pedidos
GROUP BY ID_Loja

SELECT ID_Loja, Loja FROM Loja;