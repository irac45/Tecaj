Kreirajte NumPy niz (array) od 10 nasumičnih brojeva te ga sortirajte.

import numpy as np
niz = np.random.randint(0,100,size=10)
print(np.sort(niz))
