public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (true) {

            System.out.print("\n¿Desea agregar una nueva tarea? (si/no): ");
            String pregunta = sc.nextLine().toLowerCase();

            if (pregunta.equals("si")) {

                System.out.print("¿Qué tipo de tarea desea agregar? (colegio/evento): ");
                String tipo = sc.nextLine().toLowerCase();

                if (tipo.equals("colegio")) {
                    TareaColegio.agregarTarea(sc);
                } else if (tipo.equals("evento")) {
                    TareaEvento.agregarTarea(sc);
                } else {
                    System.out.println("Opción no válida.");
                }

            } else if (pregunta.equals("no")) {

                System.out.print("¿Desea ver las tareas registradas? (si/no): ");
                if (sc.nextLine().toLowerCase().equals("si")) {
                    for (Tarea t : Tarea.listaTareas) {
                        t.mostrarTarea();
                    }
                }

                System.out.println("FIN");
                break;
            } else {
                System.out.println("Opción no válida.");
            }
        }

        // sc.close();  ← NO se cierra si se usa System.in en todo el proyecto
    }
}
