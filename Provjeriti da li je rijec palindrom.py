 Provjeriti da li je rijec palindrom, ako je vrati True, ako nije vrati False.
Provjeri da li je ulazni parametar string"""

def je_palindrom(rijec):

"""
Provjerava je li dana riječ palindrom.
:param rijec: Riječ koja se provjerava.
:return: True ako je palindrom, inače False.

"""

# Provjera je li ulazni parametar string
if not isinstance(rijec, str):
raise ValueError("Ulazni parametar mora biti string.")

# Uklanjanje razmaka i pretvaranje u mala slova za dosljednost
rijec = rijec.replace(" "").lower()

# Provjeravanje jednakosti s obrnutim stringom
return rijec == rijec[::-1]
