 DIO 3: procitati csv, izvuci title i year i vratiti listu objekata Movie"""

import csv

class MovieCsv: #Vjerovatno se klasa ne zove tako ali je preddefinirana
def __init__(self, csv_file): #preddefinirano
self.csv_file = csv_file #preddefinirano
self.movies = self.read_movies() #ovo mi pisemo

def read_movies(self): #Vjerovatno se metoda ne zove tako ali je preddefinirana
movies = []

#OVAJ DIO PIŠEMO POCETAK
with open("putanjaDoCsv.csv", 'r', newline='") as file:
reader = csv. DictReader(file)
for row in reader:
title = row['Title']
year = int(row['Year'])
movie = Movie(title, year)
movies.append(movie)

#OVAJ DIO PIŠEMO KRAJ
return movies
