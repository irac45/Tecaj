 imamo 2 csv-a sa bijelim i crvenim vinima,
moramo procitati fileove i usporediti kolonu quality 
i iscrtati usporedni graf

import pandas as pd
import matplotlib.pyplot as plt

#citamo CSV-ove


red_wines_df = pd.read_csv("red_wines.csv", delimiter=";")
white_wines_df = pd.read_csv("white_wines.csv", delimiter=";")

# izracunavamo prosjek za oba vina


avg_red_quality = red_wines_df["quality"].mean()
avg_white_quality = white_wines_df["quality"].mean()

# kreiramo chart
wine_types = ["Red Wine", "White Wine"]
average_qualities = [avg_red_quality, avg_white_quality]
plt.bar(wine_types, average_qualities, color=["crveno", "bijelo"])
plt.xlabel("Vrsta vina")
plt.ylabel("Prosjecna kvaliteta")
plt.title("Usporedna crvenih i bijelih vina (prosjek kvalitete)")
plt.show()
