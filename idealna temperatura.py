 iot: idealna temperatura je u rasponu od 18-24, idealan tlak je u rasponu od 1120 do 1500.
Ako je temperatura i tlak u ok rasponu ispisati poruku idi van,
ako nije ispisati poruku ostani doma,
Ako je jedan ili tlak ili temperatura izvan raspona napisati ostani doma """



from senzori import Senzori 


senzor = Senzori()
def check_conditions():

temp senzor.get_temperature() pressure senzor.get_humidity()
if 18 <= temp <= 24 and 1120 < pressure <= 1500:
senzor.show_message("IDI VAN")
else:
senzor.show_message("OSTANI DOMA ")
