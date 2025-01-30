
package src.hms;

public class Appointment {
    private String time;
    private String date;
    private boolean isModified;

    private Patient patient;
    private Doctor doctor;

    public String getTime() {
        return time; // Return time
    }

    public void setTime(String time) {
        this.time = time; // Set time
    }

    public String getDate() {
        return date; // Return date
    }

    public void setDate(String date) {
        this.date = date; // Set date
    }

    public boolean isModified() {
        return isModified; // Return modification status
    }

    public void setModified(boolean isModified) {
        this.isModified = isModified; // Set modification status
    }
}
