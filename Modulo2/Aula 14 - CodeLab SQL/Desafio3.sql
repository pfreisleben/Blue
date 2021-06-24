select f.numfuncionario, f.nome, f.sobrenome, f.email, (select nome from funcionarios where 
numfuncionario = f.reportaa) as "Reporta a", from funcionarios f
