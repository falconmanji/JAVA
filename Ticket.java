public class Ticket implements EstadoTicket{
    private static int counter = 1;
    private int idTicket;
    private String status;
    private String description;
    private Cliente clienteOwner;

    public Ticket(String description, Cliente clienteOwner) {
        this.idTicket = counter;
        counter++;
        this.status = "Abierto";
        this.description = description;
        this.clienteOwner = clienteOwner;
    }

    @Override
    public void changeStatus(int option) {
        if (option == 1) {
            this.status = "En Proceso";
        } else if (option == 2) {
            this.status = "Cerrado";
        }
    }

    public void showTicket() {
        System.out.println("Ticket #" + idTicket + " [" + status + "]");
        System.out.println("     Cliente: " + clienteOwner.getName());
        System.out.println("        Problema: " + description);
        System.out.println("------------------------");
    }

    public int getIdTicket() {
        return this.idTicket;
    }
}
