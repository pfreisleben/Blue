select p.codproduto as Codigo, p.nomeproduto as Nome, p.qtdestoque from produtos p 
order by p.qtdestoque asc limit 1