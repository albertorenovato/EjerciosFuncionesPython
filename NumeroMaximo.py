#MINI Calculadora: Pedirle al usuario una operación y dos números.
# Las operaciones pueden ser suma, resta, multiplicacion y division.
# Si introduce una operación diferente a estas, mostrar un menjase de error. Si la operacaion es correcta mostrar el resultado

def suma (num1, num2):
    return num1 +num2

def resta (num1, num2):
    return num1-num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1/num2

num1 = int(input('Introduce el valor del numero 1: '))
num2 = int(input('Introduce el valor del numero 2: '))
operacion = input('Intrduce que operacion quieres hacer (Suma, Resta, Multiplicacion o Division):')

if operacion == 'Suma' or operacion == 'suma':
    print(f'La suma de {num1} mas {num2} es {suma(num1,num2)}')
elif operacion == 'Resta' or operacion =='resta':
    print(f'La resta de {num1} menos {num2} es {resta(num1, num2)}')
elif operacion == 'Multiplicacion' or operacion =='multiplicacion' :
    print(f'La multiplicacion de {num1} por {num2} es {multiplicacion(num1, num2)}')
elif operacion == 'Division' or operacion =='division':
    print(f'La division de {num1} entre {num2} es {division(num1, num2)}')
else:
    print('Operacion incorrecta!!')
