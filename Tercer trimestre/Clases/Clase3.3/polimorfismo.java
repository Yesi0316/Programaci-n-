// clase base
class Animal {
    public void hablar(){
        System.out.println("el animal hace un ruido ");
    }    
}

// classe hija 1 
class Perro extends Animal{
    @Override
    public void hablar(){
         System.out.println("el perro dice; ¡Guau guau!");
        }
}

// classe hija 2 
class Gato extends Animal{
    @Override //Indica la herencia del metodo hablar de la clase base Animal
    public void hablar(){
         System.out.println("el Gato dice; ¡Miau miau!");
        }
}

// clase principal para ejecutar este programa
public class Main{
    //metodo que demuestre el polimorfismo
    public static void hacerHablar(Animal animal){
        animal.hablar();
    }

    public static void main(String[] args) {
        Perro perro = new Perro();
        Gato gato = new Gato();

        // Usar esta misma funcion con diferentes tipos de objetos
        hacerHablar(perro);
        hacerHablar(gato);
    }
}