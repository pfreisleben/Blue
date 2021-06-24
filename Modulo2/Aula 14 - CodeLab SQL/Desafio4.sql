select c.numcliente, c.nomecliente, c.sobrenomecontato, c.cidade, c.estado, sum(pag.valor) as "Valor Pago", c.limitecredito from clientes c 
inner join pagamentos pag on pag.numcliente  = c.numcliente 
group by c.numcliente 
order by sum(pag.valor) desc