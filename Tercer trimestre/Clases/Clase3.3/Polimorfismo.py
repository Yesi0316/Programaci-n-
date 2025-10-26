# clase base 
class Animal:
    def hablar(self):
        print("el animal hace un ruido ")

#clase hija 1 
class Perro(Animal):
    def hablar(self):
        print("el perro dice; ¡Guua guua!")

#clase hija 2 
class Gato(Animal):
    def hablar(self):
        print("el Gato dice; ¡Miauu miauu!")


#funcion que demuestra el polimorfismo 

def hacer_hablar(animal):
    animal.hablar()

#crear el objeto 

perro = Perro()
gato = Gato()

# Usar esta misma funcion con diferentes tipos de objetos 
hacer_hablar(perro)
hacer_hablar(gato)