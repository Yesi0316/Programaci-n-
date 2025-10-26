print("Ejercicio POO - To-Do List")

nueva_tarea= None
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
    #segundo método
    def cambiar_estado(self):
        nuevo_estado = input("Ingrese el nuevo estado de la tarea (Pendiente/En progreso/Completada): ")
        self.estado = nuevo_estado
        print(f"El estado de la tarea {self.nombre_tarea} ha sido cambiado a: {self.estado}")
    #tercer método
    def agregar_tarea(self):
        nombre_tarea = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea (Alta/Media/Baja): ")
        estado = input("Ingrese el estado de la tarea (Pendiente/En progreso/Completada): ")
        nueva_tarea = Tarea(nombre_tarea, descripcion, prioridad, estado)
        nueva_tarea.mostrar_tarea()
        lista_tareas.append(nueva_tarea)

#Clase hija 1
class Tarea_colegio(Tarea):
    def __init__(self, nombre_tarea, descripcion, prioridad, estado, materia, fecha_entrega):
        super().__init__(nombre_tarea, descripcion, prioridad, estado)
        self.materia = materia
        self.fecha_entrega = fecha_entrega 
        #primer método clase hija 1
    def mostrar_tarea(self):
        super().mostrar_tarea() #super permite que la clase hija llame a los métodos o atributos de la clase padre para no volver a escribir todo
        print(f"Materia: {self.materia} \n Fecha de entrega: {self.fecha_entrega}")
        print("-".center(50,"-"))
        #segundo método de la clase hija 1
    def cambiar_estado(self):
        super().cambiar_estado()
    #tercer método de la clase hija 1
    def agregar_tarea(self):
        super().agregar_tarea()


#clase hija 2
class Tarea_evento(Tarea):
    def __init__(self, nombre_tarea, descripcion, prioridad, estado, fecha_evento, lugar):
        super().__init__(nombre_tarea, descripcion, prioridad, estado)
        self.fecha_evento = fecha_evento
        self.lugar = lugar
        #primer método clase hija 2
    def mostrar_tarea(self):
        super().mostrar_tarea()
        print(f"Fecha del evento: {self.fecha_evento} \n Lugar: {self.lugar}")
        print("-".center(50,"-"))
        #segundo método de la clase hija 2
    def cambiar_estado(self):
         super().cambiar_estado()
    #tercer método de la clase hija 2
    def agregar_tarea(self):
        super().agregar_tarea()

#Crear las tareas desde adento del código
tarea1 = Tarea("Comprar víveres", "Comprar frutas, verduras y leche", "Alta", "Pendiente")
lista_tareas.append(tarea1)
tarea2 = Tarea_colegio("Estudiar para el examen", "Repasar los apuntes y hacer ejercicios", "Media", "En progreso", "Matemáticas", "23/04/2024")
lista_tareas.append(tarea2)
tarea3 = Tarea_evento("Ir al cumpleaños", "Comprar regalo y asistir al cumpleaños de Ana", "Baja", "Completada", "Casa de Ana", "2/05/2024")
lista_tareas.append(tarea3)

#Ingresar tareas desde consola

while True:
    pregunta= input("¿Desea agregar una nueva tarea? (si/no): ").lower()
    if pregunta == "si":
        pregunta_2= input("¿Qué tipo de tarea desea agregar? (normal/colegio/evento): ").lower()
        if pregunta_2=="normal":
            nueva_tarea.agregar_tarea(Tarea)
        elif pregunta_2=="colegio":
            nueva_tarea.agregar_tarea(Tarea_colegio)
        elif pregunta_2=="evento":
            nueva_tarea.agregar_tarea(Tarea_evento)
        else:
            print("Opciòn no valida")
    elif pregunta == "no":
        #Ver las tareas que hay en la lista
        print("Desea ver las tareas? (si/no): ")
        if input().lower() == "si":
            for tarea in lista_tareas:
                tarea.mostrar_tarea()
        else:
            print("FIN")
            break
