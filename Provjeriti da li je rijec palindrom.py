def palindrom(rijec):
    # Provjeravamo je li rijec string
    if not isinstance(rijec, str):
        return False
        
    # Brišemo razmake i pretvaramo sve znakove u mala slova
    rijec = rijec.replace(" ", "").lower()
    # Provjeravamo je li rijec jednaka svojoj inverziji
    return rijec == rijec[::-1]

def main():
    assert palindrom('kisik')
    assert palindrom('a')
    assert palindrom('')
    assert palindrom('anavolimilovana')
    assert palindrom(5) is False
    assert palindrom('aa')
    assert palindrom('ovo nije palindrom') is False
    print("Implementacija je tocna!")

if __name__ == '__main__':
    main()
