import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        GestorTickets gestor = new GestorTickets();
        int option = 0;

        do {
            System.out.println("\n ======= SISTEMA DE TICKETS =======");
            System.out.println("1.- Registrar Cliente");
            System.out.println("2.- Crear Nuevo Ticket");
            System.out.println("3.- Ver Lista de Tickets");
            System.out.println("4.- Cambiar estado de Ticket");
            System.out.println("5.- Salir");
            System.out.println("======================================");
            System.out.println("Seleccione una opcion: ");

            option = keyboard.nextInt();
            keyboard.nextLine();

            switch (option) {
                case 1:
                    System.out.print("Nombre de Cliente:");
                    String nom = keyboard.nextLine();
                    System.out.print("Cedula: ");
                    String ced = keyboard.nextLine();
                    System.out.print("Telefono: ");
                    String tel = keyboard.nextLine();

                    Cliente c = new Cliente(nom, ced, tel);
                    gestor.signClient(c);
                    System.out.println("Cliente registrado!");
                    break;

                case 2:
                    System.out.println("\n--- LOGIN PARA CREAR TICKET ---");
                    System.out.print("Ingrese su nombre de Usuario:  ");
                        String LoginName = keyboard.nextLine() ;
                    System.out.print("Ingrese su Cedula:  ");
                        String loginCed = keyboard.nextLine();

                    Cliente clienteFound = gestor   .findClientForLogin(LoginName, loginCed);

                if ( clienteFound != null) {

                    System.out.println(">> Bienvenido " + clienteFound.getName() + " . Describa su problema:");
                    System.out.print("Problema: ");
                        String issue = keyboard.nextLine();

                    Ticket newTicket = new Ticket(issue, clienteFound);
                    gestor.addTicket(newTicket);
                } else {
                    System.out.println("ERROR: Usuario no encontrado. Por favor registrese primero");
                }
                break;
                case 3:
                    System.out.println("\n--- LISTA DE TICKETS ---");
                    gestor.showAllTickets();
                    break;

                case 4:
                    System.out.print("Ingrese el ID del Ticket a modificar: ");
                    int idSought = keyboard.nextInt();
                    System.out.print("Seleccione nuevo estado: [ 1: En Proceso | 2: Cerrado]");
                    int modStatus = keyboard.nextInt();

                    gestor.handleTicket(idSought, modStatus);
                    break;

                case 5:
                    System.out.println("Saliendo...");
                    break;

                default:
                    System.out.println("Opcion invalida.");
            }

        } while (option != 5);

    }
}
