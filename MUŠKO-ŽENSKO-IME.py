MUŠKO/ŽENSKO IME

def odredi_pol(ime):
# Definirajte iznimke gdje ime završava na "a" ali nije žensko ime
iznimke = ["Matija", "Vanja", "Noa"]

# Provjeri je li ime u iznimkama i ako jest, ispišite "Ne znam"
if ime.capitalize() in iznimke:
return "Ne znam"

# Ako ime završava na "a", smatra se ženskim imenom
elif ime.endswith('a'):
return "Žensko ime"

# Ako ime ne završava na "a", smatra se muškim imenom
else:
return "Muško ime"

# Testiranje funkcije
def main():
assert odredi_pol('Anja') == "Žensko ime"
assert odredi_pol('Ivana') == 'Žensko ime'
assert odredi_pol('Petar') == 'Muško ime'
assert odredi_pol('Jana') == 'Žensko ime'
assert odredi_pol('Ivan') == 'Muško ime'
assert odredi_pol('Ana') == 'Žensko ime'
assert odredi_pol('Vanja') == 'Ne znam'
print("Implementacija je tocna!")
