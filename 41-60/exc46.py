# Crie uma lista e utilize max() para encontrar o segundo maior valor.

lista = [4, 8, 2, 9, 5]
maior = max(lista)
lista.remove(maior)
segundo_maior = max(lista)
print(segundo_maior)
