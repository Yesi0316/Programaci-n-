print("Ejercicio de tuplas")

print("Parte 1")

lista1= [1,2,3,"Rivera", 23, "azul", "fresa" ]

lista2= [45,"Yesica", 67, "azul oscuro", "a"]

num= int(input("Ingrese un número: "))
lista1.append(num)

palabra= input("Ingresé un palabra: ")

lista1.append(palabra)

print(f"lista 1 modificada= {lista1}")

print("Parte 2")

palabra2= input("Ingresé un palabra: ")

lista2.append(palabra2)

num2= int(input("Ingrese un número: "))

lista2.append(num2)

print(f"lista 1 modificada= {lista2}")

print("Parte 3")

lista3= lista1.copy()

lista3.pop()

print(f"La lista es: {lista3}")

print("Parte 4")

lista4= lista2.copy()

lista4.pop( )
lista4.pop(1)

print(F"La lista es: {lista4}")

print("Parte 5")

lista5= [lista3, lista4]

print(lista5)










