import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Tarea {  //Clase padre
    protected String nombreTarea;
    protected String descripcion;
    protected String prioridad;
    protected String estado;

    public Tarea(String nombreTarea, String descripcion, String prioridad, String estado) { //Constructor de la clase Tarea
        this.nombreTarea = nombreTarea;
        this.descripcion = descripcion;
        this.prioridad = prioridad;
        this.estado = estado;

    }
    // la lista fuera de los métodos
    private static List<Tarea> listaTareas = new ArrayList<>();

    public void mostrarTarea() { //Primer método usado para mostrar los detalles de la tarea
        System.out.println("-".repeat(30));
        System.out.println("\nTarea: " + nombreTarea);
        System.out.println("Descripción: " + descripcion);
        System.out.println("Prioridad: " + prioridad);
        System.out.println("Estado: " + estado);
    }

        public static Tarea agregarTarea() { //Segundo método usado para agregar una nueva tarea
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el nombre de la tarea: ");
        String nombreTarea = sc.nextLine();

        System.out.print("Ingrese la descripción de la tarea: ");
        String descripcion = sc.nextLine();

        System.out.print("Ingrese la prioridad de la tarea (Alta, Media, Baja): ");
        String prioridad = sc.nextLine();

        System.out.print("Ingrese el estado de la tarea (Pendiente, En Progreso, Completada): ");
        String estado = sc.nextLine();

        sc.close(); //Cerrar el 

        // Crear la nueva tarea
        Tarea nuevaTarea = new Tarea(nombreTarea, descripcion, prioridad, estado);
        
        // Agregar la tarea a la lista
        listaTareas.add(nuevaTarea);
        
        System.out.println("Tarea agregada exitosamente.");
        
        return nuevaTarea;
}

    }

// "C:\Program Files\Java\jdk-25\bin\javac.exe"  crear archivos .class terminal

// "C:\Program Files\Java\jdk-25\bin\java.exe"  crear archivos .class terminal