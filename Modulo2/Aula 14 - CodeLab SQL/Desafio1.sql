
select c.numcliente as Numero, c.nomecliente as Nome, c.sobrenomecontato as Sobrenome,
c.estado as Estado, count(p.numpedido) as "Qtd.Pedidos" from clientes c
inner join pedidos p on c.numcliente = p.numcliente 
group by c.numcliente 
order by count(p.numpedido) desc
