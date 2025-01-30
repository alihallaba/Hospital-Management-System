import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel

def create_database():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Patient (
                        Patient_id INTEGER PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        gender TEXT,
                        age INTEGER,
                        address TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Doctor (
                        Doctor_id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        address TEXT,
                        email TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Appointment (
                        Appointment_id INTEGER PRIMARY KEY,
                        Patient_id INTEGER,
                        Doctor_id INTEGER,
                        date TEXT,
                        time TEXT,
                        FOREIGN KEY(Patient_id) REFERENCES Patient(Patient_id),
                        FOREIGN KEY(Doctor_id) REFERENCES Doctor(Doctor_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Room (
                        Room_id INTEGER PRIMARY KEY,
                        Room_no TEXT,
                        Room_type TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Stay (
                        Patient_id INTEGER,
                        Room_id INTEGER,
                        Admin_id INTEGER,
                        date TEXT,
                        time TEXT,
                        PRIMARY KEY (Patient_id, Room_id),
                        FOREIGN KEY(Patient_id) REFERENCES Patient(Patient_id),
                        FOREIGN KEY(Room_id) REFERENCES Room(Room_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Admin (
                        Admin_id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        address TEXT)''')

    conn.commit()
    conn.close()

def insert_patient(name, email, gender, age, address):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Patient (name, email, gender, age, address) VALUES (?, ?, ?, ?, ?)',
                   (name, email, gender, age, address))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient inserted successfully!")

def insert_doctor(name, age, address, email):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Doctor (name, age, address, email) VALUES (?, ?, ?, ?)',
                   (name, age, address, email))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Doctor inserted successfully!")

def delete_patient(patient_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Patient WHERE Patient_id = ?', (patient_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient deleted successfully!")

def delete_doctor(doctor_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Doctor WHERE Doctor_id = ?', (doctor_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Doctor deleted successfully!")

def update_patient(patient_id, name):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Patient SET name = ? WHERE Patient_id = ?', (name, patient_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient updated successfully!")

def update_doctor(doctor_id, email):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Doctor SET email = ? WHERE Doctor_id = ?', (email, doctor_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Doctor updated successfully!")

def select_all_patients():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Patient')
    rows = cursor.fetchall()
    conn.close()
    messagebox.showinfo("Patients", "\n".join(map(str, rows)))

def select_patient_appointments():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    query = '''SELECT Patient.name, Doctor.name, Appointment.date, Appointment.time
               FROM Patient
               JOIN Appointment ON Patient.Patient_id = Appointment.Patient_id
               JOIN Doctor ON Appointment.Doctor_id = Doctor.Doctor_id'''
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    messagebox.showinfo("Appointments", "\n".join(map(str, rows)))

def main():
    create_database()

    root = Tk()
    root.title("Hospital Management System")

    Label(root, text="Insert Patient: Name, Email, Gender, Age, Address").pack()
    patient_name = Entry(root)
    patient_name.pack()
    patient_email = Entry(root)
    patient_email.pack()
    patient_gender = Entry(root)
    patient_gender.pack()
    patient_age = Entry(root)
    patient_age.pack()
    patient_address = Entry(root)
    patient_address.pack()
    Button(root, text="Insert Patient", command=lambda: insert_patient(patient_name.get(), patient_email.get(), patient_gender.get(), int(patient_age.get()), patient_address.get())).pack()

    Label(root, text="Insert Doctor: Name, Age, Address, Email").pack()
    doctor_name = Entry(root)
    doctor_name.pack()
    doctor_age = Entry(root)
    doctor_age.pack()
    doctor_address = Entry(root)
    doctor_address.pack()
    doctor_email = Entry(root)
    doctor_email.pack()
    Button(root, text="Insert Doctor", command=lambda: insert_doctor(doctor_name.get(), int(doctor_age.get()), doctor_address.get(), doctor_email.get())).pack()

    Label(root, text="Delete Patient: Patient ID").pack()
    delete_patient_id = Entry(root)
    delete_patient_id.pack()
    Button(root, text="Delete Patient", command=lambda: delete_patient(int(delete_patient_id.get()))).pack()

    Label(root, text="Delete Doctor: Doctor ID").pack()
    delete_doctor_id = Entry(root)
    delete_doctor_id.pack()
    Button(root, text="Delete Doctor", command=lambda: delete_doctor(int(delete_doctor_id.get()))).pack()

    Label(root, text="Update Patient: Patient ID, New Name").pack()
    update_patient_id = Entry(root)
    update_patient_id.pack()
    update_patient_name = Entry(root)
    update_patient_name.pack()
    Button(root, text="Update Patient", command=lambda: update_patient(int(update_patient_id.get()), update_patient_name.get())).pack()

    Label(root, text="Update Doctor: Doctor ID, New Email").pack()
    update_doctor_id = Entry(root)
    update_doctor_id.pack()
    update_doctor_email = Entry(root)
    update_doctor_email.pack()
    Button(root, text="Update Doctor", command=lambda: update_doctor(int(update_doctor_id.get()), update_doctor_email.get())).pack()

    Button(root, text="Select All Patients", command=select_all_patients).pack()
    Button(root, text="Select Patient Appointments", command=select_patient_appointments).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
