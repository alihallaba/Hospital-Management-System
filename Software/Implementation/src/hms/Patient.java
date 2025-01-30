
package src.hms;

import java.util.List;

public class Patient {
    private String name;
    private int age;
    private String gender;
    private String medicalRecord;
    private String phoneNumber;
    private String address;

    private List<Image> images;
    private List<Appointment> appointments;
    private Doctor doctor;

    public String getName() {
        return name; // Return name
    }

    public void setName(String name) {
        this.name = name; // Set name
    }

    public int getAge() {
        return age; // Return age
    }

    public void setAge(int age) {
        this.age = age; // Set age
    }

    public String getGender() {
        return gender; // Return gender
    }

    public void setGender(String gender) {
        this.gender = gender; // Set gender
    }

    public String getMedicalRecord() {
        return medicalRecord; // Return medical record
    }

    public void setMedicalRecord(String medicalRecord) {
        this.medicalRecord = medicalRecord; // Set medical record
    }

    public String getPhoneNumber() {
        return phoneNumber; // Return phone number
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber; // Set phone number
    }

    public String getAddress() {
        return address; // Return address
    }

    public void setAddress(String address) {
        this.address = address; // Set address
    }

    public void addImage(Image image) {
        images.add(image); // Add image to list
    }

    public void removeImage(Image image) {
        images.remove(image); // Remove image from list
    }

    public void addAppointment(Appointment appointment) {
        appointments.add(appointment); // Add appointment to list
    }

    public void removeAppointment(Appointment appointment) {
        appointments.remove(appointment); // Remove appointment from list
    }
}
