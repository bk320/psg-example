# Escribe un programa en Python que convierta 1000000 de 
# segundos en semanas, días, horas, minutos y segundos
dato_segundos = 1000000

semanas = dato_segundos // (7 * 24 * 60 * 60)
resto_semanas = dato_segundos % (7 * 24 * 60 * 60)
dias = resto_semanas // (24 * 60 * 60)
resto_dias = resto_semanas % (24 * 60 * 60)
horas = resto_dias // (60 * 60)
resto_horas = resto_dias % (60 * 60)
minutos = resto_horas // 60
segundos = resto_horas % 60
print(f"{dato_segundos} segundos son {semanas} semanas, {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")