 Ukloniti duplikate (u listi) u funkciji process_list koristeći 2 predefinirane funkcije """

def find_duplicates (lst):
""" funkcija koja trazi duplikate"""
seen = set()
duplicates = set()
for item in lst:
if item in seen:
duplicates.add(item)
seen.add(item)
return duplicates

def remove_duplicates(lst):
""" funkcija koja uklanja duplikate"""
return list(set(lst))

"""Ova funkcija nam je  prazna i mi moramo implementirati gornje dvije  funkcije"""
def process_list(lst):
duplicates = find_duplicates (lst)
print("Duplicates found:", duplicates)
new_list = remove_duplicates (lst)
return new_list

"""Napomena: predefinirane  funkcije možda ne izgledaju identično
