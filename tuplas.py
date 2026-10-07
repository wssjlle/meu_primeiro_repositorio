# programa para testar tuplas e listas e converter tuplas em listas e listas em tuplas  

lista_cidades = ["Blumenau", "Indaial", "Gaspar", "Pomerode", "Timbó"]  

print("Cidades na lista:")
for cidade in lista_cidades:
    print(cidade)

lista_cidades.append("Ilhota")

print("Cidades na lista após adicionar Ilhota:")
for cidade in lista_cidades:
    print(cidade)

tupla_cidades = tuple(lista_cidades)

print("Cidades na tupla:")
for cidade in tupla_cidades:
    print(cidade)

print("Será gerado um erro, pois tuplas são imutáveis e não podem ter elementos removidos.")

tupla_cidades.remove("Gaspar")


