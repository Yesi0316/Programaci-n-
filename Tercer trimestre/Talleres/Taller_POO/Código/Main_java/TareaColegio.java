import java.util.Scanner;

class TareaColegio extends Tarea {
    private String materia;
    private String fechaEntrega;

    public TareaColegio(String nombreTarea, String descripcion, String prioridad, String estado,
                         String materia, String fechaEntrega) {
        super(nombreTarea, descripcion, prioridad, estado);
        this.materia = materia;
        this.fechaEntrega = fechaEntrega;
    }

    @Override
    public void mostrarTarea() {
        super.mostrarTarea();
        System.out.println("Materia: " + materia);
        System.out.println("Fecha de entrega: " + fechaEntrega);
    }

    public static void agregarTarea(Scanner sc) {
        String[] datosBase = Tarea.agregarTareaBase(sc);

        System.out.print("Ingrese la materia: ");
        String materia = sc.nextLine();

        System.out.print("Ingrese la fecha de entrega (dd/mm/aaaa): ");
        String fecha = sc.nextLine();

        Tarea_colegio nueva = new Tarea_colegio(
                datosBase[0], datosBase[1], datosBase[2], datosBase[3],
                materia, fecha
        );

        listaTareas.add(nueva);
        nueva.mostrarTarea();
    }
}
