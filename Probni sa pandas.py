Probni

import pandas
import matplotlib.pyplot as plot

data = pandas.read_csv("cars.csv", sep=";")
data['Weight'] = pandas.to_numeric(data['Weight'], errors="coerce")

#print(data.dtypes)
data.groupby('Origin')['Weight'].plot(kind='hist', alpha=0.5, legend=True)
plot.xlabel("Weight")
plot.ylabel("Freq")
plot.title("Weight chart")
plot.show()
