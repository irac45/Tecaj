def zamijeni(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def najmanji(lista, i, j):
    return lista.index(min(lista[i: j + 1]))

def sortiraj(ulaznalista):
    duzinaliste = len(ulaznalista)
    for i in range(duzinaliste):
        # Pronalazi poziciju najmanjeg elementa od i do kraja liste
        pozicijaNajmanjeg = najmanji(ulaznalista, i, duzinaliste - 1)
        # Zamjenjuje trenutni element s najmanjim elementom nakon njega
        zamijeni(ulaznalista, i, pozicijaNajmanjeg)
    return ulaznalista

def main():
    # Test liste 1
    test_lista_1 = [5, 4, 3, 2, 1]
    sortirana_lista_1 = sortiraj(test_lista_1) 
    assert sortirana_lista_1 == [1, 2, 3, 4, 5]
    print(f"Test 1 prošao: {sortirana_lista_1}")

    # Test liste 2
    test_lista_2 = [-1, 0, 2, 5, 8]
    sortirana_lista_2 = sortiraj(test_lista_2) 
    assert sortirana_lista_2 == [-1, 0, 2, 5, 8]
    print(f"Test 2 prošao: {sortirana_lista_2}")

    # Test liste 3
    test_lista_3 = [5, 4, 1, 2, 3, 10, 20, 100, 99]
    sortirana_lista_3 = sortiraj(test_lista_3) 
    assert sortirana_lista_3 == [1, 2, 3, 4, 5, 10, 20, 99, 100]
    print(f"Test 3 prošao: {sortirana_lista_3}")

if __name__ == "__main__":
    main()
