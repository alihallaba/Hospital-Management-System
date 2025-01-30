
package src.hms;

import java.util.List;

public class Department {
    private String name;

    private List<Doctor> doctors;

    public String getName() {
        return name; // Return name
    }

    public void setName(String name) {
        this.name = name; // Set name
    }

    public void addDoctor(Doctor doctor) {
        doctors.add(doctor); // Add doctor to list
    }

    public void removeDoctor(Doctor doctor) {
        doctors.remove(doctor); // Remove doctor from list
    }
}
