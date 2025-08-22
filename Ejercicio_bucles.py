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

print("Ejercicio #4")

c=1
pares= []
impares=[]

while c>=10:
    num=int(input("Inresé un número:"))
    c+=1
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Sus números pares son: {pares} /n Sus números impares son: {impares}")














