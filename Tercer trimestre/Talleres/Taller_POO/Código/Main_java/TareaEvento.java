class TareaEvento extends Tarea {
    private String fechaEvento;
    private String lugar;

    public TareaEvento(String nombreTarea, String descripcion, String prioridad, String estado,
                        String fechaEvento, String lugar) {
        super(nombreTarea, descripcion, prioridad, estado);
        this.fechaEvento = fechaEvento;
        this.lugar = lugar;
    }

    @Override
    public void mostrarTarea() {
        super.mostrarTarea();
        System.out.println("Fecha del evento: " + fechaEvento);
        System.out.println("Lugar: " + lugar);
    }

    public static void agregarTarea(Scanner sc) {
        String[] datosBase = Tarea.agregarTareaBase(sc);

        System.out.print("Ingrese la fecha del evento (dd/mm/aaaa): ");
        String fecha = sc.nextLine();

        System.out.print("Ingrese el lugar del evento: ");
        String lugar = sc.nextLine();

        Tarea_evento nueva = new Tarea_evento(
                datosBase[0], datosBase[1], datosBase[2], datosBase[3],
                fecha, lugar
        );

        listaTareas.add(nueva);
        nueva.mostrarTarea();
    }
}

