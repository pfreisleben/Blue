""" telefones = [("Pedro", "1245-1250"), ("Ricardo", "536363"),
             ("Pedro", "124212"), ("Fernando", "15155465"),
             ("Eduardo", "22352235")]
print(telefones)
contatos = dict(telefones)
print(contatos)
print(contatos.get("Pedro")) """

vingadores = {
    "Chris Evans": "Capitão América",
    "Mark Ruffalo": "Hulk",
    "Tom Hiddleton": "Loki",
    "Chris Hemworth": "Thor",
    "Robert Downey Jr": "Homem de Ferro",
    "Scarlett Johansson": "Viúva Negra"
}
nome = input("Digite o nome do ator")
print(vingadores.get("Chris Evans"))
print(vingadores.get(nome, "O nome não existe"))
