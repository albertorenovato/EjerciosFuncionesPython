#Programa que indica el signo Zodical, pidiendo al usuario su dia y mes de nacimento
# Tema: Funciones
# Alberto Diaz 14 Julio del 2022
def signo(day ,month):
    if (21<= day <=30 and month ==3 ) or (1 <= day <= 20 and month == 4):
        return 'Aries'
    elif (21<= day <= 30 and month == 4) or (1<= day <=20 and month ==5 ):
        return 'Tauro'
    elif (21<= day <= 30 and month == 5) or (1<= day <= 21 and month == 6):
        return 'Geminis'
    elif (22 <=day <= 30 and month == 6) or (1<= day <=22 and month == 7):
        return 'Cancer'
    elif (23 <= day <= 30 and month == 7) or (1<= day <=23 and month == 8):
        return 'Leo'
    elif (24 <= day <= 30 and month == 8) or (1<= day <= 22 and month == 9):
        return 'Virgo'
    elif (23<= day <= 30 and month == 9) or (1 <= day <= 22 and month == 10):
        return 'Libra'
    elif (23 <= day <= 30 and month == 10) or (1<= day <=22 and month == 11):
        return 'Escorpion'
    elif(23 <= day <= 30 and month == 11) or (1<= day <= 21 and month == 12):
        return 'Sagitario'
    elif(22<= day <= 30 and month==12) or (1<= day <= 20 and month == 1):
        return 'Capricornio'
    elif(21<=day <= 30 and month ==1) or (1<=day <= 19 and month ==2):
        return 'Acuario'
    elif(20<=day <=30 and month==2) or (1<=day <= 20 and month == 3):
        return 'Piscis'
    else:
        return 'Fecha invalida'



dayUser = int(input('Introduce tu dia de nacimiento: '))
monthUser = int(input('Introduce el tu mes de nacimento (1 al 12): '))

print(f'Tu signo zodiacal es {signo(dayUser,monthUser)}')
