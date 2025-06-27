print("Ejemplo de diccionario")

auto= {
"marca": "Ford",
"modelo": "Mustang", #IMPORANTE: las variables hay que separarlas con comas
"año": 2022,
"color": "Azul oscuro",
"dueño":"Carlos",
"ciudad_creación": "Palmira"
}

print(f"El modelo es: {auto["modelo"]}")

auto["año"]=2023 #cambiar la variable año por cualquier valor

print(f"El año de la compra del auto: {auto['año']}")

auto["placa"]= "YP7866" #Añadimos un nuevo valor a nuestro diccionario

print(f"La placa de su vehiculo es: {auto['placa']}")

del auto["modelo"] #Borra esta variable del diccionario, es más fuerte que el .pop
auto.pop("marca") #Borra esta variable, es menos fuerte que el del

print(f"Mi diccionario luego de modificarlo= {auto}")
