
package src.hms;

import java.util.List;

public class Doctor {
    private String name;
    private String specialization;

    private Department department;
    private List<Patient> patients;

    public String getName() {
        return name; // Return name
    }

    public void setName(String name) {
        this.name = name; // Set name
    }

    public String getSpecialization() {
        return specialization; // Return specialization
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization; // Set specialization
    }

    public void addPatient(Patient patient) {
        patients.add(patient); // Add patient to list
    }

    public void removePatient(Patient patient) {
        patients.remove(patient); // Remove patient from list
    }
}
