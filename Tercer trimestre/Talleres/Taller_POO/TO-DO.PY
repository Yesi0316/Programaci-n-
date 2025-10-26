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
    #segundo método
    @classmethod
    def agregar_tarea(cls):
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
        print(f"\n Materia: {self.materia} \n Fecha de entrega: {self.fecha_entrega}")
        #segundo método de la clase hija 1
    @classmethod
    def agregar_tarea(cls):
        nombre_tarea, descripcion, prioridad, estado = super().agregar_tarea()
        materia = input("Ingrese la materia de la tarea: ")
        fecha_entrega = input("Ingrese la fecha de entrega de la tarea (dd/mm/aaaa): ")
        nueva_tarea = cls(nombre_tarea, descripcion, prioridad, estado, materia, fecha_entrega)
        lista_tareas.append(nueva_tarea)
        return nueva_tarea


#clase hija 2
class Tarea_evento(Tarea):
    def __init__(self, nombre_tarea, descripcion, prioridad, estado, fecha_evento, lugar):
        super().__init__(nombre_tarea, descripcion, prioridad, estado)
        self.fecha_evento = fecha_evento
        self.lugar = lugar
        #primer método clase hija 2
    def mostrar_tarea(self):
        super().mostrar_tarea_colegio()
        print(f"\n Fecha del evento: {self.fecha_evento} \n Lugar: {self.lugar}")
        #segundo método de la clase hija 2
    @classmethod
    def agregar_tarea(cls):
        nombre_tarea, descripcion, prioridad, estado = super().agregar_tarea()
        fecha_evento = input("Ingrese la fecha del evento (dd/mm/aaaa): ")
        lugar = input("Ingrese el lugar del evento: ")
        nueva_tarea = cls(nombre_tarea, descripcion, prioridad, estado, fecha_evento, lugar)
        lista_tareas.append(nueva_tarea)
        return nueva_tarea

#Crear las tareas desde adento del código
tarea1 = Tarea("Comprar víveres", "Comprar frutas, verduras y leche", "Alta", "Pendiente")
lista_tareas.append(tarea1)
tarea2 = Tarea_colegio("Estudiar para el examen", "Repasar los apuntes y hacer ejercicios", "Media", "En progreso", "Matemáticas", "23/04/2024")
lista_tareas.append(tarea2)
tarea3 = Tarea_evento("Ir al cumpleaños", "Comprar regalo y asistir al cumpleaños de Ana", "Baja", "Completada", "Casa de Ana", "2/05/2024")
lista_tareas.append(tarea3)

#Ingresar tareas desde consola

nueva_tarea= "vacio"

while True:
    pregunta= input("¿Desea agregar una nueva tarea? (si/no): ").lower()
    if pregunta == "si":
        pregunta_2= input("¿Qué tipo de tarea desea agregar? (normal/colegio/evento): ").lower()
        if pregunta_2=="normal":
            Tarea.agregar_tarea()
        elif pregunta_2=="colegio":
           Tarea_colegio.agregar_tarea()
        elif pregunta_2=="evento":
            Tarea_evento.agregar_tarea()
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

