#print("Ejercicio #1") #Suma de números hasta  0

# num= []

# while True:
#     numero=int(input("Ingresé un número: "))
#     num.append(numero)
#     if numero==0:
#         print(f"La suma de los valores es: {sum(num)}")
#         break

# print("Ejercicio #2")

# while True:
#     con= input("Ingresé la contraseña: ")
#     print("No es la contraseña")
#     if con=="python123":
#         print("Contraseña correcta")
#         break

# print("Ejercicio #3")

# productos=[]

# while True:
#     p= input("Ingresé un producto (si ya no quiere agregar mas productos escriba fin): ").lower()
#     productos.append(p)
#     if p=="fin":
#         productos.pop()
#         print(f"Tu lista de productos es: {productos}")
#         break

# print("Ejercicio #4")

# c=1
# pares= []
# impares=[]

# while c<=10:
#     num=int(input("Inresé un número:"))
#     c+=1
#     if num%2==0:
#         pares.append(num)
#     else:
#         impares.append(num)

# print(f"Sus números pares son: {pares} \n Sus números impares son: {impares}")

# print("Ejercicio #5")

# notas= []
# i=1

# while True:
#     nota= float(input("Ingresé una nota (maximo 5 notas): "))
#     notas.append(nota)
#     i+=1
#     if i==5:
#         notas.pop(-1)
#         print(notas)
#         promedio= sum(notas)/len(notas)
#         print(f"El promedio de las notas fue: {promedio}")
#         break

# print("Ejercicio #6")

# num= int(input("Ingrése un número: ")) #Se le pide al usuario ingresar un número

# i=1 #Se inicia el multipicador en 1

# print(f"\n inicia el contador en 1 taba del {num}: ") #Se le informa al usuario del inicio del contador

# while i <=10: #Repite la sentencia hasta que i sea mayor a 10 y se detiene
#     print(f"{num}x{i}= {num*i}") #Imprime la multiplicación
#     i+=1 #Se le suma 1 aal multiplicador para poder hallar la tabla de multiplicación hasta el 10

# x= int(input("Ingresé un número: "))

# print("Ejercicio #7")
# ad=-2
# while True:
#     adivinar= int(input("Ingresé un número: "))
#     if adivinar==ad:
#      print("Adivinaste el número")
#      break
#     elif adivinar<ad:
#        print("El número es mayor al ingresado")
#     else:
#        print("El número es menor al ingresado")

# print("Ejercicio #8")

# fruta= ("fresa","manzana","pera","cambur")

# while True:
#     fruta_adivinar= input("Ingresé una fruta: ").lower()
#     if fruta_adivinar==fruta[0] or fruta_adivinar==fruta[1] or fruta_adivinar==fruta[2] or fruta_adivinar==fruta[3]:
#         print(f"La fruta {fruta_adivinar} esta en la lista, FELICIDADES :)")
#         break
#     else:
#         print("La fruta no esta en la lista :(")

# print("Ejercicio 9")

# traduccion= {"play":"Jugar", 
#              "draw":"dibujar",
#              "enjoy":"disfrutar",
#              "summer":"Verano",
#              "colder":"Más frio"}

# while True:
#     palabra= input("Ingresé una palabra para traducir a español del inglés: ").lower()
#     if traduccion.get(palabra)==None:
#         print("Su palabra no esta en el sistema")
#     else:
#         print(f"La palabra en español es: {traduccion[palabra]}")

# print("Ejercicio 10")

# op=[]
# c=0
# a=1

# while True: 
#     print("Escoja la operación a realizar: \n 1.Suma \n 2.Resta \n 3.Multiplicación \n 4.División \n 5. Salir del programa")
#     tip_op=int(input("Ingresé el número de la operación a realizar: "))
#     a+=1
#     num_op= float(input("Ingrese un número para operar:"))
#     num_op2=float(input("Ingrese un número para operar:"))
#     c+=1
#     op.append(num_op)
#     op.append(num_op2)
#     if c==1 and tip_op==1:
#         print(f"La suma de los números es {sum(op)}")
#     elif c==1 and tip_op==2:
#         resta=op[0]-op[1]
#         print(f"La resta de los números es: {resta}")
#     elif c==1 and tip_op==3:
#         mul=op[0]*op[1]
#         print(f"La resta de los números es: {mul}")
#     elif c==1 and tip_op==4:
#         div=op[0]/op[1]
#         print(f"La resta de los números es: {div}")
#     elif tip_op==5:
#         print("Bye")
#         break

# print("Ejercicio 11")
        
# informacion={}

# while True:
#     nombre= input("Ingresé su nombre (Si ya no quiere ingresar más nombres ponga salir): ")

#     if nombre=="salir":
#         print(f"La información ingresada fue: {informacion}")
#         break
#     else:
#         edad= int(input("ingresé su edad: "))
#         informacion[nombre]=edad

# print("Ejercicio 12")

# colores= ["azul","rojo", "salmon","gris","violeta"]

# while True:
#     color= input("Ingresé un color: ").lower()
#     if color==colores[0] or color==colores[1] or color==colores[2] or color==colores[3] or color==colores[4]:
#         print(f"el color {color} esta en la lista, FELICIDADES :)")
#         break
#     else:
#         print("No es el color")

# print("Ejercicio 13")

# num= int(input("Ingrése un número: ")) 
# i=1 
# print(f"\n inicia el contador en 1 taba del {num}: ") 
# while i<=5:
#     print(f"{num}^{i}= {num**i}") 
#     i+=1 

# print("Ejercicio 14")

# i=1
# cuadrados=[]

# while i<=5:
#     nume= float(input("Ingresé un número para elevar al cuadrado: "))
#     op= nume**2
#     cuadrados.append(op)
#     i+=1
# print(f"El cuadrado de sus números ingresados es: {cuadrados}")

# print("Ejercicio 15")

# nota_final={}

# while True:
#     estudiante= input("Ingresé el nombre del estudiante (Si ya no quiere ingresar más estudiantes ponga fin): ").lower()

#     if estudiante=="fin":
#         print(f"Las notas finales ingresadas fue: {nota_final}")
#         break
#     else:
#         nota_f= int(input("ingresé la nota final del estudiante: "))
#         nota_final[estudiante]=nota_f