
package src.hms;

public class Bed {
    private String bedNumber;
    private boolean isOccupied;

    private Patient patient;

    public String getBedNumber() {
        return bedNumber; // Return bed number
    }

    public void setBedNumber(String bedNumber) {
        this.bedNumber = bedNumber; // Set bed number
    }

    public boolean isOccupied() {
        return isOccupied; // Return occupancy status
    }

    public void setOccupied(boolean isOccupied) {
        this.isOccupied = isOccupied; // Set occupancy status
    }
}
