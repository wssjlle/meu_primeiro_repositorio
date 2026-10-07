# teste de uso de listas no python

lista_cidades = ["Blumenau", "Indaial", "Gaspar", "Pomerode", "Timbó"]

# Adicionando elementos à lista
lista_cidades.append("Ilhota")

# Removendo elementos da lista
lista_cidades.remove("Gaspar")

# Acessando elementos da lista
print("Primeira cidade:", lista_cidades[0])

print("Cidades na lista:")
for cidade in lista_cidades:
    print("-", cidade)

# classificando a lista em ordem alfabética
lista_cidades.sort()

print("Cidades na lista (em ordem alfabética):")
for cidade in lista_cidades:
    print("-", cidade)


