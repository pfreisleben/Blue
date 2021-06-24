select f.nome, f.sobrenome, f.email, l.cidade, l.pais, l.telefone from funcionarios f 
inner join lojas l on l.codloja = f.codloja
where f.cargo = 'President'