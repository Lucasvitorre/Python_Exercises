-- FUNCOES DE AGREGAÇOES - COUNT / COUNT (*) / DISTINCT / SUM / AVG / MIN-MAX

-- COUNT
--  Objetivo da função COUNT é retornar o valor de valores de uma coluna - * Ignora os valores nulos
SELECT 
    COUNT(Telefone)
FROM clientes;

-- COUNT (*)
-- RETORNA A QUANTIDADE TOTAL DE LINHAS DE UMA TABELA
SELECT
    COUNT(*)
FROM clientes;

--COUNT(DISTINCT)
--RETORNA A CONTAGEM DISTINTA DE VALORES DE UMA TABELA
SELECT
    COUNT(DISTINCT categoria)
FROM categorias;

-- SUM
--RETORNA A SOMA TOTAL DOS VALORES DE UMA COLUNA
SELECT
    SUM(Receita_venda)
FROM pedidos;

--AVG
--RETORNA A MEDIA DE UMA COLUNA
SELECT
    AVG(Receita_venda)
FROM pedidos;

-- MIN
-- RETORNA O MINIMO DE UMA COLUNA
SELECT
    MIN (Receita_venda)
FROM pedidos;

-- MAX
-- RETORNA A MAXIMA DE UMA COLUNA
SELECT
    MAX (Receita_venda)
FROM pedidos;

-- MAX IDADE 
SELECT MIN (Data_Nascimento) FROM clientes;