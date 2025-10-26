print("Ejercicio POO - To-Do List")

#Lista de tareas
lista_tareas = []
class Tarea:
    #definir los atribuos
    def __init__(self, nombre_tarea, descripcion, prioridad ,estado):
        self.nombre_tarea = nombre_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
    #primer mètodo
    def mostrar_tarea(self):
        print("-".center(50,"-"))
        print(f"Tarea: {self.nombre_tarea} \n Descripción: {self.descripcion} \n Prioridad: {self.prioridad} \n Estado: {self.estado}")
        print("-".center(50,"-"))

#Crear las tareas desde adento del código
tarea1 = Tarea("Comprar víveres", "Comprar frutas, verduras y leche", "Alta", "Pendiente")
lista_tareas.append(tarea1)
tarea2 = Tarea("Estudiar para el examen", "Repasar los apuntes y hacer ejercicios", "Media", "En progreso")
lista_tareas.append(tarea2)
tarea3 = Tarea("Hacer ejercicio", "Correr 30 minutos y hacer estiramientos", "Baja", "Completada")
lista_tareas.append(tarea3)

#Ingresar tareas desde consola

while True:
    pregunta= input("¿Desea agregar una nueva tarea? (si/no): ").lower()
    if pregunta == "si":
        nombre_tarea = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea (Alta/Media/Baja): ")
        estado = input("Ingrese el estado de la tarea (Pendiente/En progreso/Completada): ")
        nueva_tarea = Tarea(nombre_tarea, descripcion, prioridad, estado)
        nueva_tarea.mostrar_tarea()
        lista_tareas.append(nueva_tarea)
    elif pregunta == "no":
        #Ver las tareas que hay en la lista
        print("Desea ver las tareas? (si/no): ")
        if input().lower() == "si":
            for tarea in lista_tareas:
                tarea.mostrar_tarea()
        else:
            print("FIN")
            break
