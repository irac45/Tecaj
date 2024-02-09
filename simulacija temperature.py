# Napišite skriptu koja svake sekunde (1s) sa senzora pročita
# temperaturu.
# Na temelju pročitanih vrijednosti skripta treba na
# zaslon (display) ispisati pripadajuću poruku.
# Idealna temperatura je u rasponu od 18-24.
# Ako je temperatura idealnom rasponu treba na zaslon ispisati:
# - "IDEALNO".
# Ako je temperatura izvan raspona treba ispisati:
# - "HLADNO" ako je ispod ili "VRUCE" ako je iznad.

sensors = Sensors()

while True:
temperature = sensors.get_temperature()

if 18<= temperature <=24:
print("IDEALNO")
elif temperature <18:
print("HLADNO")
else:
print("VRELO")

time.sleep(1)
