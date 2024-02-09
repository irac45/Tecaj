import tkinter as tk


 DIO 1: buttonima dati funkcionalnost povlacenja iz baze i iz csv-a"""


class MovieApp:
def_init__(self):
master tk.Tk()
self.master = master
self.master.title("Movie App")



# OVAKO IZGLEDA ZADATAK


self.povuci_iz_baze = tk.Button(master, text="Button 1")
self.povuci_iz_baze.grid(row=1, column=0, padx=5)
self.povuci_iz_csv = tk.Button(master, text="Button 2")
self.povuci_iz_csv.grid(row=1, column=1, padx=5)



# OVO JE RIJESENJE

self.povuci_iz_baze = tk.Button(master, text="Button 1", command=self.povuci_podatke)
self.povuci_iz_baze.grid(row=1, column=0, padx=5)
self.povuci_iz_csv = tk.Button(master, text="Button 2", command=self.povuci_csv)
self.povuci_iz_csv.grid(row=1, column=1, padx=5)



" U principu samo treba dodati command=self.imeMetode
imeMetode ćete naći u toj klasi par linija nize. Radi se o dvije metode i imaju logičan naziv
