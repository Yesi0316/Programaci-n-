print("Ejercicio: calcula el número mayor de dos números")

a= float(input("Ingrese un número: "))
b= float(input("Ingrese un número: "))

if a<b: 
    print(f"{b} es el mayor")

elif b<a:
    print(f"{a} es mayor")

else: 
    print("Los dos números son iguales")