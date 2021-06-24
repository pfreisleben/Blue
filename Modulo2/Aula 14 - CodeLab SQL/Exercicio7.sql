select p.codproduto as Codigo, p.nomeproduto as Nome, p.precosugerido from produtos p 
order by p.precosugerido asc limit 1