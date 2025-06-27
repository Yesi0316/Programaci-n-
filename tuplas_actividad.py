mi_tupla= (1,2,3)
mi_lista= list(mi_tupla)

print(mi_lista)

mi_lista.append("agrego")

tupla= tuple(mi_lista)

print(tupla)


print("Ejercicio 1")

frutas= ("manzana", "pera")

frutas_listas= list(frutas)

añadir= input("Ingrese una fruta: ")
frutas_listas.append(añadir)

frutas= tuple(frutas_listas)

print(f"tu lista de compras es: {frutas}")

print("Ejercicio 2")

calificaciones= (4.2, 3.8)

lista_calificaciones= list(calificaciones)
añadir_2= float(input("Ingrese una nota: "))
lista_calificaciones.append(añadir_2)
calificaciones= tuple(lista_calificaciones)
print(f"Las notas son: {calificaciones}")


print("Ejercicio ")

tu= ("Ana","Gómez")

tu_lista= list(tu)

añade= int(input("Ingrsé su documento de identidad: "))

tu_lista.append(añade)

tu= tuple(tu_lista) 

print(f"Su nombre es: {tu[0]}, tu apellido es: {tu[1]}, tu número de identidad es: {tu[2]}")






