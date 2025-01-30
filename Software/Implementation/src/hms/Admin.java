
package src.hms;

import java.util.List;

public class Admin {
    private String name;
    private String address;

    private List<Department> departments;
    private List<Doctor> doctors;
    private List<Patient> patients;

    public String getName() {
        return name; // Return name
    }

    public void setName(String name) {
        this.name = name; // Set name
    }

    public String getAddress() {
        return address; // Return address
    }

    public void setAddress(String address) {
        this.address = address; // Set address
    }

    public void addDepartment(Department department) {
        departments.add(department); // Add department to list
    }

    public void removeDepartment(Department department) {
        departments.remove(department); // Remove department from list
    }

    public void addDoctor(Doctor doctor) {
        doctors.add(doctor); // Add doctor to list
    }

    public void removeDoctor(Doctor doctor) {
        doctors.remove(doctor); // Remove doctor from list
    }

    public void addPatient(Patient patient) {
        patients.add(patient); // Add patient to list
    }

    public void removePatient(Patient patient) {
        patients.remove(patient); // Remove patient from list
    }
}
