
select p.codproduto as "Cod. Produto", p.nomeproduto as Nome, p.linhaproduto as "Linha Produto",
p.precosugerido as "Preco Sugerido", count(distinct det.numpedido) as "Qtd.Pedidos" from produtos p
inner join detalhespedidos det on det.codproduto = p.codproduto 
group by p.codproduto
order by count(distinct det.numpedido) desc

