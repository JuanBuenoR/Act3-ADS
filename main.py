#En este ejercicio he creado una "calculadora" básica que nos permita realizar las 4 operaciones básicas entre dos números, 
# el usuario nos proveera el operador matematico y los dos numeros a operar. 
#  
# Importamos las funciones desde funciones.py
from funciones import suma, resta, multiplicacion, division

#Definimos la función "main", que será nuestro punto de entrada al programa por parte del usuario
def main():
    # Mensaje de bienvenida y opciones de uso
    print("Bienvenidos a esta sencilla calculadora entre dos números")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    # Obtenemos el operador por parte del usuario
    operador = int(input("Ingresa una opción: "))
 # Obtenemos l3os dos numeros por parte del usuario
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))

  #Validamos el operador y realizamos la operación solicitada detallando el proceso en la respuesta.
    if operador == 1:
        resultado = suma(num1, num2)
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif operador == 2:
        resultado = resta(num1, num2)
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif operador == 3:
        resultado = multiplicacion(num1, num2)
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    elif operador == 4:
        if num2 != 0:
            resultado = division(num1, num2)
            print(f"La división de {num1} y {num2} es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero")
    else:
        print("Error: Opción inválida")


if __name__ == "__main__":
    main()

    