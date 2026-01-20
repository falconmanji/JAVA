public class Persona {
    protected String name;
    protected String identification;

    public Persona(String name, String identification) {
        this.name = name;
        this.identification = identification;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getIdentification() {
        return identification;
    }

    public void setIdentification(String identification) {
        this.identification = identification;
    }
}
