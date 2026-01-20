import java.util.ArrayList;

public class GestorTickets{
    private ArrayList<Ticket> listTickets;
    private ArrayList<Cliente> listClients;

    public GestorTickets() {
        this.listTickets = new ArrayList<>();
        this.listClients = new ArrayList<>();
    }

    public void addTicket(Ticket t) {
        listTickets.add(t);
        System.out.println("SISTEMA: Guardado con exito!");
    }

    public void handleTicket(int idRequested, int newOption) {
        boolean found = false;

        for (Ticket t : listTickets) {
            if (t.getIdTicket() == idRequested) {
                t.changeStatus(newOption);
                System.out.println("SISTEMA: Estado actualizado.");
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("SISTEMA: No se encontro algun ticket con ese ID.");
        }
    }

    public void showAllTickets() {
        if (listTickets.isEmpty()) {
            System.out.println("No hay tickets registrados.");
        } else {
            for (Ticket t : listTickets) {
                t.showTicket();
            }
        }
    }

    public void signClient(Cliente newClient) {
        listClients.add(newClient);
        System.out.println("SISTEMA: Cliente " + newClient.getName() + " guardado.");
    }

    public Cliente findClientForLogin(String name, String id) {
        for (Cliente c : listClients) {

            if (c.getName().equalsIgnoreCase(name) && c.getIdentification().equals(id)) {
                return c;
            }
        }
        return null;
    }

}
