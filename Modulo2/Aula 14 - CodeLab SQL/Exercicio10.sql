select p.codproduto as Codigo, p.nomeproduto as Nome, sum(d.quantidadepedida)
from produtos p 
inner join detalhespedidos d on d.codproduto = p.codproduto 
inner join pedidos ped on ped.numpedido = d.numpedido 
where ped.status = 'Shipped'
group by p.codproduto