# print("EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS \n Ejercicio #1") #Verifica si un número es positivo negativo o 0

# num1= float(input("Ingresé un número: "))

# if num1<0:
#     print(f"{num1} es negativo")
# elif num1>0:
#     print(f"{num1} es positivo")
# else:
#     print(f"{num1} es igual a 0") 
# print("Ejercicio # 2") 

# num3=float(input("Ingresé el número:"))
# num4=float(input("Ingresé el número:"))
# if num3<num4:
#     print(f"{num4} es el mayor")
# else:
#     print(f"{num3} es el mayor")

# print("Ejercicio # 3") #par o impar

# num2= float(input("Ingresé un número: "))

# if num2%2==0:
#     print(f"El número {num2} es par")
# else:
#     print(f"El número {num2} es impar ")

# print("Ejercicio # 4") #número entre 10 y 20 

# num20= float(input("Ingresé un número: "))

# if num20>=10 and num20<20:
#     print(f"El número {num20} esta entre 10 y 20")
# else:
#     print(f"El número {num20} no esta entre 10 y 20")

# print("Ejercicio 5") #El mayor de tres números

# num4= float(input("Ingrese un número: "))
# num5= float(input("Ingrese un número: "))
# num6= float(input("Ingrese un número: "))

# if num4>num5 and num4>num6:
#     print(f"{num4} es el número mayor")

# elif num5>num4 and num5>num6:
#     print(f"{num5} es el mayor")

# else:
#     print(f"{num6} es el mayor")

# print("Ejercicio 6") #precio final con 10% de descuento si la compra es mayor a 100$

# total= float(input("Ingrese su total: "))

# if total>=100:
#     op2= total-((total*1)/100)
#     print(f"Su total con el descuento será {op2}")
# else: 
#     print("No aplica el descuento para su compra")

# print("Ejercicio 7") #Puede votar?

# edad= int(input("Ingresé su edad: "))

# if edad>=18:
#     print("Puede votar")
# else:
#     print("No puede votar")

# print("Ejercicio 8") #descuento a clientes (solo si es VIP 20%)

# precio= float(input("Ingrese su precio: "))
# cliente= input("Ingrese el tipo del cliente (VIP o normal): ").upper()

# if cliente=="VIP":
#     op3= precio-((precio*20)/100)
#     print(f"Su total es {op3}")

# else:
#     print(f"Su precio es: {precio}")

# print("Ejercicio 9") #Multiplo de 3 y de 5

# num7= float(input("Ingrese un número: "))
# op4= num7%3 
# op5= num7%5

# if op4==0 and op5==0:
#     print("Su número es divisible de 3 y 5")

# elif op4==0:
#     print("Tu número es solo divisible entre 3")

# elif op5==0:
#     print("Tu número es solo divisible entre 5")

# else:
#     print("Tu número no es divisible ni entre 3 ni entre 5")

# print("Ejercicio 10") #Multiplo de números ingresados

# num8= float(input("Ingrese un número:"))
# div= float(input("Ingrese un número para saber si el divisible: "))
# div2= float(input("Ingrese un número para saber si el divisible: "))

# op6= num8%div
# op7= num8%div2

# if op6==0 and op7==0:
#     print(f"Tu número {num8} es divisible entre los dos números")

# elif op6==0:
#     print(f"Tu número {num8} solo es divisible entre {div}")

# elif op7==0:
#     print(f"Tu número {num8} solo es divisible entre {div2}")

# else: 
#     print("No es divisible entre ningun número")


# print("Ejercicio 11")

# lista=[float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: "))]

# if lista[2]>10:
#     print(f"El número de la lista {lista[2]} es mayor a 10")
# elif lista[2]<=10:
#     print(f"El número de la lista {lista[2]} es menor o igual a 10")

# print("Ejercicio 12")

# numeros=[float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: "))]

# if numeros[0]==7 or  numeros[1]==7 or  numeros[2]==7 or  numeros[3]==7:
#     print("El número 7 esta en los números")
# else:
#     print("El número 7 no esta en los números ingresados")

# print("Ejercicio 13")

# l_suma=[float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: "))]
# op_s=l_suma[0]+l_suma[1]
# if op_s>10:
#     print(f"La suma de los dos primeros números de la cadena es {op_s} y un número mayor ")
# else:
#     print(f"la suma de los dos primeros números de la cadena es {op_s} y NO es un número alto")

# print("Ejercicio 14")

# names=[input("Ingrese un nombre: ").upper(), input("Ingrese un nombre: ").upper(),input("Ingrese un nombre: ").upper(),input("Ingrese un nombre: ").upper()]

# if names[-1]=="MARTA":
#     print(f"el nombre final: {names[-1]} \n Nombre correcto ")
# else:
#     print("El nombre es incorrecto")

# print("Ejercicio 15")

# colores= [input("Ingresé un color: "),input("Ingresé un color: "),input("Ingresé un color: ")]

# if colores[1]=="azul":
#     colores.remove("azul")
#     color_nuevo= input("Ingresé un núvo color para remplazar el azul: ")
#     colores.insert(1,color_nuevo)
#     print(f"La lista actualizada sin el azul es: {colores}")
# else:
#     print(f"La lista de colores no sufrió cambios, es: {colores}")

# print("Ejercicio 16")
# num_orden=(float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: "))) 

# if num_orden[0]<num_orden[-1]:
#     print(f"La lista {num_orden} esta en orden ascendente")
# else:
#     print(f"La lista {num_orden} esta en orden descendente")

# print("Ejercicio 17")

# edades=(int(input("Ingrese una edad: ")),int(input("Ingrese una edad: ")),int(input("Ingrese una edad: "))) 

# if edades[1]>30:
#     print(f"{edades[1]} es mayor a 30")
# elif edades[1]==30:
#     print(f"La edad {edades[1]} es igual a 30")
# else:
#     print(f"La edad {edades[1]} es menor a 30")

# print("Ejercicio 18")

# num_orden=(float(input("Ingrese un número: ")),float(input("Ingrese un número: ")),float(input("Ingrese un número: ")))

# if num_orden[1]==2:
#     lista2=list(num_orden)
#     lista2.remove(2)
#     usuario_num= float(input("Ingresé un número para remplazar el 2:"))
#     lista2.insert(1,usuario_num)
#     num_orden2=tuple(lista2)
#     print(f"Su tupla quedo {num_orden2}")
# else:
#     print(f"La tupla no se modifico sigue: {num_orden}")

# print("Ejercicio 19")

# coordenada= (float(input("Ingresé la coordenada del eje x: ")),float(input("Ingresé la coordenada del eje y:")))
# if coordenada[1]>5:
#     print(f"La cordena {coordenada[1]} alta")
# else:
#     print(f"La coordenada {coordenada[1]} es baja")

# print("Ejercicio 20")

# tupla_1= (float(input("Ingresé la un número: ")),float(input("Ingresé otro número:")))
# tupla_2= (float(input("Ingresé la un número: ")),float(input("Ingresé otro número:")))

# if tupla_1==tupla_2:
#     print("Las tuplas son iguales")
# else:
#     print("Las tplas son diferentes")



























































































 
