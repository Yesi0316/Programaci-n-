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

# print("Ejercicio 13")
# estudiantes= {"Áaron": float(input("Ingresé la nota de Áaron: ")), "Alejandra": float(input("Ingresé la nota de Alejandra: ")),"Santiago":float(input("Ingresé la nota de Áaron: "))}

# op_dicc= (estudiantes["Áaron"]+estudiantes["Alejandra"]+ estudiantes["Santiago"])/3

# print(f"El promedio es: {op_dicc}")

# print("Ejercicio 14")

# salarios=[int(input("Ingresé salario: ")),int(input("Ingresé salario: ")),int(input("Ingresé salario: " )),int(input("Ingresé salario: " )),int(input("Ingresé salario: " ))]
# aum_salario=[]
# aum_salario.append(salarios[0]+((salarios[0]*10)/100))
# aum_salario.append(salarios[1]+((salarios[1]*10)/100))
# aum_salario.append(salarios[2]+((salarios[2]*10)/100))
# aum_salario.append(salarios[3]+((salarios[3]*10)/100))
# aum_salario.append(salarios[4]+((salarios[4]*10)/100))

# print(f"Los salarios aumentados un 10%:\n {aum_salario[0]}\n {aum_salario[1]}\n {aum_salario[2]}\n {aum_salario[3]}\n {aum_salario[4]} ")

# print("Ejercicio 15")

# sin_imp= {"pan": 98, "arroz": 89, "aceite":50, "azucar": 12, "cafe": 780}
# con_imp= [ ]

# imp1= float(input("Ingresé el impuesto para agregar al pan: " ))
# imp2= float(input("Ingresé el impuesto para agregar al arroz: " ))
# imp3= float(input("Ingresé el impuesto para agregar al aceite: " ))
# imp4= float(input("Ingresé el impuesto para agregar a la azúcar: " ))
# imp5= float(input("Ingresé el impuesto para agregar al café: " ))

# con_imp.append(sin_imp["pan"]+ ((sin_imp["pan"]*imp1)/ 100))
# con_imp.append(sin_imp["arroz"]+ ((sin_imp["arroz"]*imp1)/ 100))
# con_imp.append(sin_imp["aceite"]+ ((sin_imp["aceite"]*imp1)/ 100))
# con_imp.append( sin_imp["azucar"]+ ((sin_imp["azucar"]*imp1)/ 100))
# con_imp.append( sin_imp["cafe"]+ ((sin_imp["cafe"]*imp1)/ 100))

# print(f"El precio de los productos más los impuestos son: \n Pan: {con_imp[0]}  \n arroz: {con_imp[1]}  \n aceite: {con_imp[2]}  \n azúcar: {con_imp[3]} \n café: {con_imp[4]}")

# print("Ejercicio 16")

# lis_eda=[int(input("Ingrése una edad: ")), int(input("Ingrése una edad: ")), int(input("Ingrése una edad: ")), int(input("Ingrése una edad: "))] 

# mayor= (lis_eda[0]>=18)+(lis_eda[1]>=18)+(lis_eda[2]>=18)+(lis_eda[3]>=18)
# menor= len(lis_eda)-mayor

# print(f"En este grupo hay:\n mayores de edad: {mayor} \n menores de edad: {menor}  ")

# print("Ejercicio 17")

# dinero= float(input("Ingrese un cantidad de dinero (dólares):"))

# conver_di= ((dinero*0.85), (dinero*4088.25), (dinero*144.88))

# print(f"sus doláres en: \n Euros: {conver_di[0]} \n Pesos colombianos: {conver_di[1]} \n Yenes japoneses:{conver_di[2]}")

# print("Ejercicio 18")

# name1= input("Ingresé el nombre del producto1: ")
# name2=input("Ingresé el nombre del producto2: ")
# name3= input("Ingresé el nombre del producto3: ")

# p4=  int(input("Ingresé la cantidad de productos vendidos del producto 1: "))
# p5= int(input("Ingresé la cantidad de productos vendidos del producto 2: "))
# p6=int(input("Ingresé la cantidad de productos vendidos del producto 3: ")) 

# vent= {name1:p4, name2:p5, name3:p6}

# suma= vent[name1]+vent[name2]+vent[name3]

# print(f"La cantidad de productos vendidos es: {suma}")

# print("Ejercicio 19")

# temperaturas= [float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")),float(input("Ingresé una temperatura: ")) ]

# temp_mayor= [(temperaturas[0]*(temperaturas[0]>30)),(temperaturas[1]*(temperaturas[1]>30)),(temperaturas[2]*(temperaturas[2]>30)),(temperaturas[3]*(temperaturas[3]>30)),(temperaturas[4]*(temperaturas[4]>30)),(temperaturas[5]*(temperaturas[5]>30)),(temperaturas[6]*(temperaturas[6]>30)),(temperaturas[7]*(temperaturas[7]>30)),(temperaturas[8]*(temperaturas[8]>30)),(temperaturas[9]*(temperaturas[9]>30)),0 ] #con el 0 al final se evita el error de que no haya 0 paara quitar
# temp_menor= [(temperaturas[0]*(temperaturas[0]<10)),(temperaturas[1]*(temperaturas[1]<10)),(temperaturas[2]*(temperaturas[2]<10)),(temperaturas[3]*(temperaturas[3]<10)),(temperaturas[4]*(temperaturas[4]<10)),(temperaturas[5]*(temperaturas[5]<10)),(temperaturas[6]*(temperaturas[6]<10)),(temperaturas[7]*(temperaturas[7]<10)),(temperaturas[8]*(temperaturas[8]<10)),(temperaturas[9]*(temperaturas[9]<10)),0 ]

# temp_mayor.sort() #Ordena la lista
# print(temp_mayor)
# i_m=temp_mayor.index(0) #Busca el primer 0
# i_m2=temp_mayor.index(0,temp_mayor.count(0)-1) #Busca el último 0
# del temp_mayor[i_m:i_m2+1] #Quita todos los 0

# temp_menor.sort()
# print(temp_menor)
# i_m3=temp_menor.index(0)
# i_m4=(temp_menor.index(0,temp_menor.count(0)-1)+1)+i_m3 #Se le suma el index de los otros 0 para eliminar los negativos
# del temp_menor[i_m3:i_m4]
# 41
# print(f"Las temperaturas mayores a 30 son: {temp_mayor}\n Las temperaturas menores a 10 son {temp_menor}")

# print("Ejercicio 20")

# actualizar=[278.9,8219828.9989,3783.93,2390.78,234.32]

# print(f"Estos son los precios: {actualizar}")

# bus= float(input("Ingresé un salario para eliminar: "))

# busqueda=actualizar.index(bus)

# actualizar.pop(busqueda)

# agre= float(input("Agregue un salario: "))

# actualizar.append(agre)
# actualizar.sort

# print(f"La lista de precios actualizada es: {actualizar}")


#






