package src.hms;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        DatabaseHandler dbHandler = new DatabaseHandler();
        Connection connection = null;
        ResultSet resultSet = null;

        try {
            // Get a database connection
            connection = dbHandler.getConnection();
            System.out.println("Connected to the database!");

            //  Execute a query
            String query = "SELECT * FROM Doctor";
            resultSet = dbHandler.executeQuery(connection, query);

            // Process the result set
            System.out.println("Doctor Data:");
            while (resultSet.next()) {
                int DoctorID = resultSet.getInt("Doctor_iD"); // Ensure this matches the column name
                String name = resultSet.getString("Doctor_name"); // Ensure this matches the column name
                String Age = resultSet.getString("Age"); // Ensure this matches the column name
                String Email = resultSet.getString("email"); // Ensure this matches the column name

                System.out.println("ID: " + DoctorID + ", Name: " + name + ", Age: " + Age + ", Email: " + Email);
            }
        } catch (ClassNotFoundException e) {
            System.err.println("JDBC driver not found!");
            e.printStackTrace();
        } catch (SQLException e) {
            System.err.println("Error connecting to the database!");
            e.printStackTrace();
        } finally {
            //  Close the resources
            dbHandler.closeResources(connection, null, resultSet);
        }
    }
}
