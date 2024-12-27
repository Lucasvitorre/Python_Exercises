-- LEFT JOIN / RIGHT JOIN / INNER JOIN / FULL JOIN
-- UTILIZANDO O INNER JOIN

-- Faça uma consulta que tenha como resultado todas as colunas da tabela de pedidos e as colunas Lojas, Gerente
-- E telefone.

SELECT
    pedidos.*,
    lojas.Loja,
    lojas.Gerente,
    lojas.telefone

FROM pedidos
INNER JOIN lojas
    ON pedidos.ID_Loja = pedidos.ID_Loja;
--
--

--
--

--
--