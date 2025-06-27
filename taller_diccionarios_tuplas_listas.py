# print("Taller de Aplicación listas, tuplas y diccionarios")

# print("Ejercicio 1")

# lista= []

# p1= int(input("Ingrese una calificación: "))
# p2= int(input("Ingrese una calificación: "))
# p3= int(input("Ingrese una calificación: "))

# lista.append(p1)
# lista.append(p2)
# lista.append(p3)


# op= (lista[0]+lista[1]+lista[2])/3

# print(f"El promedio de sus tres notas es: {op}")


# print("Ejercicio 2")

# pro1= {"harina": 78, "arroz": 23, "pan": 45}

# print(f"Precios originales: {pro1}")

# por1= float(input("Ingrese el porcentaje de aumento de la harina (%): "))
# por2= float(input("Ingrese el porcentaje de aumento del arroz (%) : "))
# por3= float(input("Ingrese el porcentaje de aumento del pan (%): "))

# pro1["harina"]= pro1["harina"] +(pro1["harina"]*por1)/100
# pro1["arroz"]= pro1["arroz"]+(pro1["arroz"]*por1)/1008
# pro1["pan"]= pro1["pan"]+(pro1["pan"]*por1)/100

# print(f"Ahora los productos cuestan: {pro1}")

# print("Ejercicio 3")

# t1= int(input("Ingrese una temperatuta en celsius para convertir a Fahrenheit: "))
# t2= int(input("Ingrese una temperatuta en celsius para convertir a Fahrenheit: "))
# t3= int(input("Ingrese una temperatuta en celsius para convertir a Fahrenheit: "))
# t4= int(input("Ingrese una temperatuta en celsius para convertir a Fahrenheit: "))
# t5= int(input("Ingrese una temperatuta en celsius para convertir a Fahrenheit: "))

# temperaturas= (t1, t2,t3,t4,t5)

# op2= (temperaturas[0]*9/5)+32
# op3= (temperaturas[1]*9/5)+32
# op4= (temperaturas[2]*9/5)+32
# op5= (temperaturas[3]*9/5)+32
# op6= (temperaturas[4]*9/5)+32

# temperaturas_aumento= (op2,op3,op4,op5,op6)

# print(f"""Las temperaturas en celsius son: {temperaturas}
# en fahrenheit son: {temperaturas_aumento}""")

# print("Ejercicio 4")

# lista2= [int(input("Ingresé una edad: ")), int(input("Ingresé una edad: ")), int(input("Ingresé una edad: ")), int(input("Ingresé una edad: ")), int(input("Ingresé una edad: "))]

# op_edad= (lista2[0]+lista2[1]+lista2[2]+lista2[3]+lista2[4])//5

# print(f"""La mayor edad es: {max(lista2)}
# La menor edad es: {min(lista2)}
# El promedio de edades es: {op_edad}""")

# print("Ejercicio 5")

# frutas= {"fresa":22, "Mango": 12, "uva": 189}

# kilos= int(input("Ingrese los kilos que lleva de fresa: "))
# kilos1= int(input("Ingrese los kilos que lleva de fresa: "))
# kilos2= int(input("Ingrese los kilos que lleva de fresa: "))

# op7= frutas["fresa"]*kilos
# op8= frutas["Mango"]*kilos1
# op9= frutas["uva"]*kilos2

# compra= op7+op8+op9

# print(f"El total de la compra será: {compra} $")

# print("Ejercicio 6")

# num_tupla= (int(input("Ingrese un número: ")),int(input("Ingrese un número: ")), int(input("Ingrese un número: ")), int(input("Ingrese un número: ")),int(input("Ingrese un número: ")) )

# print(f"La suma de sus números es: {sum(num_tupla)}")

# print("Ejercicio 7")

# precios= {}

# nom1= input("Ingrése el nombre del producto uno: ")
# nom2= input("Ingrése el nombre del producto dos: ")
# nom3= input("Ingrése el nombre del producto tres: ")

# pre1= int(input("Ingrese el precio del producto uno: "))
# pre2= int(input("Ingrese el precio del producto dos: "))
# pre3= int(input("Ingrese el precio del producto tres: "))

# precios[nom1]=pre1
# precios[nom2]=pre2
# precios[nom3]=pre3

# lista_precios= [precios]

# print(f"Su lista de productos y precios es: {lista_precios}")

# print("Ejercicio 8")

# precios_usuario= [65, 242, 23, 78.90, 12.9]
# usuario= []

# print(f"Precios originales: {precios_usuario}")

# descuento= float(input("Ingrese un descuento (%): "))

# usuario.append(precios_usuario[0]+((precios_usuario[0]*descuento)/100))
# usuario.append(precios_usuario[1]+((precios_usuario[0]*descuento)/100))
# usuario.append(precios_usuario[2]+((precios_usuario[0]*descuento)/100))
# usuario.append(precios_usuario[3]+((precios_usuario[0]*descuento)/100))
# usuario.append(precios_usuario[4]+((precios_usuario[0]*descuento)/100))

# print(f"Sus nuevos precios son: {usuario} ")

# print("Ejercicio 9")

# notas= (int(input("Ingresé una nota: ")), int(input("Ingresé una nota: ")), int(input("Ingresé una nota: ")), int(input("Ingresé una nota: ")))

# print(f"La mayor nota es: {max(notas)} y la menor nota es:  {min(notas)} ")

# print("Ejercicio 10")

# conversiones= {"km":1000, "m":1, "cm": 0.01}

# uni= (input("Ingrese la unidad para la conversión a metros (km, m,cm): "))

# cant= (int(input("Ingrese la cantidad a convertir: ")))

# op10= conversiones[uni]*cant

# print(f"El resultado de la conversión es: {op10}")

# print("Ejercicio 11")

# plista=[int(input("Ingrese el precio de un producto: ")), int(input("Ingrese el precio de un producto: ")), int(input("Ingrese el precio de un producto: ")), int(input("Ingrese el precio de un producto: ")), int(input("Ingrese el precio de un producto: "))] 

# result=[]

# result.append(plista[0]+((plista[0]*19)/100))
# result.append(plista[1]+((plista[0]*19)/100))
# result.append(plista[2]+((plista[0]*19)/100))
# result.append(plista[3]+((plista[0]*19)/100))
# result.append(plista[4]+((plista[0]*19)/100))

# print(f"Sus precios con el IVA son: {result}")

# print("Ejercicio 12")

# a= int(input("Ingresé un número: "))
# b= int(input("Ingresé un número: "))

# tuplab=(a+b,a-b,b*a,a/b)

# print(f"La suma de los números es: {tuplab[0]}\n la resta es: {tuplab[1]}\n la multiplicación es: {tuplab[2]}\n la división es: {tuplab[3]} ")

print("Ejercicio 13")
estudiantes= {"Áaron": 5, "Alejandra": 3, "Santiago": 3.2}

op_dicc= (estudiantes["Áaron"]+estudiantes["Alejandra"]+ estudiantes["Santiago"])/3

print(f"El promedio es: {op_dicc}")






























