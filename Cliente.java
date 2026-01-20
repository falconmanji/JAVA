public class Cliente extends Persona{
    private String phone;

    public Cliente(String name, String identification, String phone) {
        super(name, identification);
        this.phone = phone;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}
