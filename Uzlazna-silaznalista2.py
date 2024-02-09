def sortiraj_listu(lista): #evo ovo treba u zadatku napraviti
for i in range(len(lista)):
min_index = najmanji(lista, i)
zamijeni(lista, i, min_index)
return lista
# Primjer upotrebe
lista = [5, 3, 8, 6, 2, 7, 4, 1]
sortirana_lista = sortiraj_listu(lista)
print("Sortirana lista:", sortirana_lista)
def main():
assert sortiraj_listu([1, 3, 6, 8, 2]) == [1, 2, 3, 6, 8]
assert sortiraj_listu([9, 9, 7, 9, 5, 1]) == [1, 5, 7, 9, 9, 9]
assert sortiraj_listu([5, 6, 8, 9, 3, 5, 1]) == [1, 3, 5, 5, 6, 8, 9]
assert sortiraj_listu([1, 3, 2]) == [1, 2, 3]
print('Implementacija je ispravna')
