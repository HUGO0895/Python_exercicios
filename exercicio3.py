dia= int(input("Dia:"))
hora=int(input('Hora:'))
min=int(input("Minutos:"))
seg=int(input("Segundos:"))
total_segundos=dia*24*60**2+hora*60**2+min*60+seg
print(total_segundos)