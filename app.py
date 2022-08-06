import datetime

now = datetime.datetime.now()
now_ohnems = now.replace(microsecond=0)

print(
    "Hallo, mein Wurms! <br><br>Heute schreiben wir folgendes Datum:",
    str(now_ohnems))

wurmizeit = datetime.datetime(2022, 8, 27, 12, 00, 00)
untilwurmi = wurmizeit - now_ohnems
#print(str(untilwurmi))

#total t
tsecs = untilwurmi.total_seconds()
#print(tsecs)

#total
wurmimin = tsecs / 60
#print(wurmimin)
wurmihours = wurmimin / 60
#print(wurmihours)
wurmidays = wurmihours / 24
#print(wurmidays)

#differenz
hours = wurmidays - int(wurmidays)
hours = hours * 24
#print(hours)
mins = wurmihours - int(wurmihours)
mins = mins * 60
#print(mins)

print(
    f"<br>Und jetzt kannst du dich endlich über mein vollbrachtes Werk freuen!<br>Juhuuuuuu!!! <br> Der Countdown sagt: <br>Nur mehr {int(wurmidays)} Tage und  <br>{int(hours)} Stunden und <br>{int(mins)} Minuten <br>bis zur großen Wurmi-Reunion am 27.08. um (circa 12:00)! <br><br><3 <3 <3"
)