public class Tecnico extends Persona{
    private String skill;

    public Tecnico(String name, String identification, String skill) {
        super(name, identification);
        this.skill = skill;
    }

    public String getSkill() {
        return skill;
    }

    public void setSkill(String skill) {
        this.skill = skill;
    }
}
