select p.codproduto as Codigo, p.nomeproduto as Nome, p.qtdestoque from produtos p 
order by p.qtdestoque desc limit 1