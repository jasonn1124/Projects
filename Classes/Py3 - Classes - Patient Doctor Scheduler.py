"""
Patient / Doctor Scheduler
	Create a patient class and a doctor class. 
	Setup a scheduling program
		A doctor can only handle 16 patients during an 8 hr work day.
"""

import subprocess
import datetime as dt
import numpy as np
import pandas as pd

def cls():
    subprocess.call("cls", shell = True)

class patient:
    name = ""
    date_created = dt.date.today()
    appointment = [] # List of datetime objects
    
class doctor:
    name = ""
    schedule = [] # List of appointments, to cap at 16 objects

def main_menu():
    cls()
    print("Welcome to the scheduler.\n"
        "Please select an option.\n"
        )
    print(
        "1 | Register a new patient\n"
        "2 | View list of patients\n"
        "3 | Book a new appoinment\n"
        "4 | Change or delete an appointment\n"
        "5 | Exit this script\n"
        )
    try:
        user_input = int(input("Ready>>> "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        input("Press enter to continue..")
    else:
        if user_input == 1:
            register_patient()
        elif user_input == 2:
            view_patient_list()
        elif user_input == 3:
            book_appointment()
        elif user_input == 4:
            edit_appointment()
        elif user_input == 5:
            cls()
            print("Exiting script.")
            input("Press enter to continue..")
            global is_running
            is_running = False
        else:
            print("\nInvalid input. Please enter a number from one of the "
                "menu options."
                )
            input("Please press enter to continue..")

def register_patient():
    # Creates a new patient in the database and saves it.
    register_loop = True
    while register_loop:
        cls()
        print("New patient registration")
        new_patient = patient
        new_patient.name = input("Please enter patient name: ")
        
        cls()
        print("Patient details\n\n"
            "Patient name: {0}\n"
            "Patient created: {1}\n".format(new_patient.name, new_patient.date_created)
            )
        print("Please confirm if the above details are correct.")
        try_loop = True
        while try_loop:
            try:
                user_input = input("Y/N >>> ").upper()
            except ValueError:
                print("\nAn invalid input was received. Please enter 'Y' or 'N'.")
                input("Press enter to continue..")
            else:
                try_loop = False
                if user_input == "Y":
                    register_loop = False
                    pass # Save data and commit to file
                elif user_input == "N":
                    print("\nData discarded. Please enter new details.")
                    input("Press enter to continue..")
                else:
                    print("\nAn invalid input was received. Please enter 'Y' or 'N'.")
                    input("Press enter to continue..")
                    try_loop = True
            
    
def view_patient_list():
    pass
    
def book_appointment():
    pass
    
def edit_appointment():
    pass

def save_data():
    # Saves schedule data to a .csv file
    pass
    
def read_data():
    # Reads schedule data from a .csv file and loads it into the script
    pass

# Script execution begins here
is_running = True
while is_running:
    main_menu() 
