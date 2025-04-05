# Crie uma lista e utilize min() para encontrar o segundo menor valor.

lista = [4, 8, 2, 9, 5]
menor = min(lista)
lista.remove(menor)
segundo_menor = min(lista)
print(segundo_menor)
