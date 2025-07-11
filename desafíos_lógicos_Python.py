# print("Ejercicio 1")

# edad= int(input("Ingresé su edad: "))

# if edad>=18 and edad<=65:
#      print("Es mayor de edad")
# elif edad<18:
#      print("Es menor de edad")
# else:
#      print("Es un adulto mayor")

# print("Ejercicio 2")

# estatura= float(input("Ingresé su estatura (m): "))

# if estatura<1.5:
#     print("Eres considerado bajo")
# elif estatura>=1.5 and estatura<1.8:
#     print("Eres considerado de estatura media")
# else:
#     print ("Eres considerado alto")

# print("Ejercicio 3")

# num= float(input("Ingrese un número: "))
# op= num%2
# op2= num%3

# if op==0 and op2==0:
#     print("Su número es divisible de 2 y 3")

# elif op==0:
#     print("Tu número es solo divisible entre 2")

# elif op2==0:
#     print("Tu número es solo divisible entre 3")

# else:
#     print("Tu número no es divisible ni entre 2 ni entre 3")

# print("Ejercicio 4")

# num2= str(float(input("Ingresé un número con decimales:")))
# cadena= num2.split(".")
# cuenta= len(cadena[1])

# if cuenta==1:
#     print("Tiene un solo decimal su número")
# elif cuenta==2:
#     print("El número tiene dos decimales")
# else: 
#     print(f"El número tiene {cuenta} decimales")

# print("Ejercicio 5")

# pais= input("Ingresé un país: ")
# paises= ("Colombia", "Perú", "Argentina", "México")

# if pais==paises[0] or pais==paises[1] or  pais==paises[2] or  pais==paises[3]:
#     print("Su país esta en la lista")

# else: 
#     print("Su país no esta en la lista")

# print("Ejercicio 6")

# tipo= input("Ingresé su tipo de sangre (A,B,AB,O):")

# compatibilidad= {"A":"B", "B":"A","AB":"O","O":"AB"}

# if tipo=="A":
#     print(f"Su tipo de sangre es compatible con {compatibilidad['A']} ")
# elif tipo=="B":
#     print(f"Su tipo de sangre es compatible con {compatibilidad['B']} ")
# elif tipo=="AB":
#     print(f"Su tipo de sangre es compatible con {compatibilidad['AB']} ")
# elif tipo=="O":
#     print(f"Su tipo de sangre es compatible con {compatibilidad['O']} ")
# else: 
#     print("Su tipo de sangre no es compatible o esta mal igresada")

# print("Ejercicio 7")

# temperatura=float(input("Ingrese una temperatura (°C): "))

# if temperatura<10:
#     print("Esta haciendo frío")
# elif temperatura>=10 and temperatura<=25:
#     print("Esta templado")
# else:
#     print("Hace calor")

# print("Ejercicio 8")

# nume1= float(input("Ingresé un número: "))
# nume2= float(input("Ingresé un número: "))
# operacion= int(input("Ingresé la operación (sumar:1, restar=2, multiplicar:3): "))

# if operacion==1:
#     op3= nume1+nume2
#     print(f"El resultado de su operación de suma es: {op3}")
# elif operacion==2:
#     op4= nume1-nume2
#     print(f"El resultado de restar los dos números es: {op4}")
# elif operacion==3:
#     op5= nume1*nume2
#     print(f"El resultado de multiplicar sus dos números es: {op5}")

# print("Ejercicio 9")

# mes= int(input("Ingresé un número para saber a que mes del año corresponde (1-12): "))
# meses= {"1":"Enero", "2":"Febrero","3":"Marzo", "4":"Abril", "5": "Mayo", "6":"Junio", "7":"Julio", "8":"Agosto","9":"Septiembre","10":"Octubre", "11":"Noviembre", "12":"Diciembre"}

# if mes==1:
#     print(f"El mes 1 del año es: {meses['1']}")
# elif mes==2:
#     print(f"El mes 2 del año es: {meses['2']}")
# elif mes==3:
#     print(f"El mes 3 del año es: {meses['3']}")
# elif mes==4:
#     print(f"El mes 4 del año es: {meses['4']}")
# elif mes==5:
#     print(f"El mes 5 del año es: {meses['5']}")
# elif mes==6:
#     print(f"El mes 6 del año es: {meses['6']}")
# elif mes==7:
#     print(f"El mes 7 del año es: {meses['7']}")
# elif mes==8:
#     print(f"El mes 8 del año es: {meses['8']}")
# elif mes==9:
#     print(f"El mes 9 del año es: {meses['9']}")
# elif mes==10:
#     print(f"El mes 10 del año es: {meses['10']}")
# elif mes==11:
#     print(f"El mes 11 del año es: {meses['11']}")
# elif mes==12:
#     print(f"El mes 12 del año es: {meses['12']}")
# else:
#     print("Su número esta mal ingresado y no cumple con los parámetros")

# print("Ejercicio 10")

# numeros= int(input("Ingresé un número de 4 dígitos: "))
# num_dig= list(numeros)

# if num_dig[0]==1:
#     print("Su número incia por 1")
# elif num_dig[0]==2:
#     print("Su número inicia por 2")
# else:
#     print(f"Súmero inicia por: {num_dig[0]}")

# print("Ejercicio 11")

# palabra= input("Ingrese una palabra: ")
# palabra_2= list(palabra)

# if palabra_2[0]=="a" or palabra_2[0]=="e" or palabra_2[0]=="i" or palabra_2[0]=="o" or palabra_2[0]=="u":
#     print("Inicia una con una vocal")
# elif palabra_2[0]==float:
#     print("Inicia con un número")
# else:
#     print("Incia con una consonante")

# print("Ejercicio 12")

# fruta= input("Ingresé una fruta: ")
# frutas= ["manzana", "pera","piña"]

# if fruta==frutas[0]:
#     print(f"El precio de la fruta {fruta[0]} es de 8000")  
# elif fruta==frutas[1]:
#     print(f"El precio de la fruta {fruta[1]} es de 18000")
# elif fruta==frutas[2]:
#     print(f"El precio de la fruta {fruta[2]} es de 2000")
# else:
#    print("Su fruta no esta disponible")

# print("Ejercicio 13")

# nota= float(input("Ingresé su nota (0-5): "))

# if nota<3:
#     print("Perdiste la materia")
# elif nota>=3 and nota<=4:
#     print("Aprobado")
# elif nota<=5:
#     print("Aprovado con excelencia")

# else: 
#     print("La nota no es válida")

# print("Ejercicio 14")

# num6= float(input("Ingrese un número: "))
# op6= num6%4
# op7= num6%6

# if op6==0 and op7==0:
#     print("Su número es divisible de 4 y 6")

# elif op6==0:
#     print("Tu número es solo divisible entre 4")

# elif op7==0:
#     print("Tu número es solo divisible entre 6")

# else:
#     print("Tu número no es divisible ni entre 4 ni entre 6")

# print("Ejercicio 15")

# usuario= input("Ingresé su nombre de usuario: ")
# contraseña= input("Ingresé su nombre de contraseña: ")

# claves_de_usuarios= {"Maria":"Maria123", "Gamer344":"Hola344", "HOLA":"adios"}

# if usuario=="Gamer344" and contraseña==claves_de_usuarios["Gamer344"]:
#     print("Bienvevido a su cuenta")
# elif usuario=="Maria" and contraseña==claves_de_usuarios["Maria"]:
#     print("Bienvevido a su cuenta")
# elif usuario=="HOLA" and contraseña==claves_de_usuarios["HOLA"]:
#     print("Bienvevido a su cuenta")
# else:
#     print("Usuario o contraseña incorrectos")

# print("Ejercicio 16")

# edad2= int(input("Ingresé su edad: "))

# if edad2<=12:
#      print("Eres un niño")
# elif edad2>=13 and edad2<=17:
#      print("Es un adolecente")
# elif edad2>=18 and edad2<=65:
#      print("Es mayor de edad")
# elif edad2<18:
#      print("Es menor de edad")
# else:
#      print("Es un adulto mayor")

# print("Ejercicio 17")

# ciudad= input("Ingrese el nombre de una ciudad: ")
# ciudades= ("Bogóta","Berlín","Caracas","Kabul", "Ciudad de Panáma")
# if ciudad==ciudades[0]or ciudad==ciudades[1]or ciudad==ciudades[2]or ciudad==ciudades[3]or ciudad==ciudades[4]:
#     print("Es una ciudad Capital")
# else:
#     print("Es una ciudad secundaria")

# print("Ejercicio 18")

# compra= float(input("Ingrese el valor de una compra: "))

# if compra>=200:
#     op8= compra-((compra*15)/100)
#     print(f"Su compra menos el descunto es de: {op8}")
# elif compra>=100 and compra<200:
#     op9= compra-((compra*10)/100)
#     print(f"Su compra menos el descunto es de: {op9}")
# else:
#     print("No aplica ningún descuento")

# print("Ejercicio 19")

# name= input("Ingresa tu nombre: ")
# horas= float(input("Ingresé el número de horas trabajadas: "))

# if horas>=40:
#     salario= (horas*10000)+(((horas*10000)*20)/100)
#     print(f"Su salario es de {salario}")
# else:
#  salario2= (horas*10000)
#  print(f"Su salario es de {salario2}")

# print("Ejercicio 20")

# nota3= float(input("Ingresé su nota (0-100): "))

# if nota3<50:
#     print("Insuficiente")
# elif nota3>=50 and nota3<=79:
#     print("Aceptable")
# elif nota3>=80 and nota3<=100:
#     print("Excelencia")

# else: 
#     print("La nota no es válida")












