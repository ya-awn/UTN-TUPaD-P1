#1 verifica si es mayor de 18 años
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#2 verifircar si la nota esta aprobada o no 
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3  verificar si el numero es par 
numero = int(input("ingrese un numero par: "))
if numero % 2 == 0:
    print("ha ingresado un numero par")
else:
    print("por favor, ingrese un numero par")

#4 clasificar segun edad 
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif edad < 18:
    print("Adolecente")
elif edad < 30:
    print("Adulto joven")
else:
    print("Adulto")

# 5 Validar longitud de contraseña
print("=== Longitud de contraseña 8 a 14 caracteres ===")
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6 Calcular sesgo en lista aleatoria
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)

print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda_valor}")

if media > mediana > moda_valor:
    print("Sesgo positivo")
elif media < mediana < moda_valor:
    print("Sesgo negativo")
elif media == mediana == moda_valor:
    print("Sin sesgo")
else:
    print("No cumple con las condiciones estrictas de sesgo")

# 7 Agregar signo de exclamación si termina en vocal
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)

# 8 Transformar nombre según elección
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para MAYÚSCULAS, 2 para minúsculas, 3 para Capitalizado: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# 9 Clasificación de terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# 10 Determinar estación del año
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese número de mes (1-12): "))
dia = int(input("Ingrese día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Primavera")
else:
    print("Datos inválidos")

