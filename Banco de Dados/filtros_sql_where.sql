--    Criando Filtros no SQL utilizando WHERE   --
-----------------------------------------------------

-- Filtros de números
SELECT *
from produtos
WHERE Preco_Unit >= 400;

SELECT *
from produtos
WHERE Preco_Unit = 3100;
-- Filtros de Textos
SELECT *
FROM produtos
WHERE Marca_Produto = "DELL";
-- Filtros de Datas
SELECT *
FROM pedidos
WHERE Data_Venda = "2019-01-03";

-- Multiplos Filtros utilizando os três de cima.
-- Utilizando AND em OR

SELECT *
FROM clientes
WHERE Estado_Civil = "S" AND Sexo = "M";
------------------------------------------------
SELECT *
FROM produtos
WHERE Marca_Produto = "DELL" OR Marca_Produto = "SAMSUNG";