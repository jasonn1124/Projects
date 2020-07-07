"""
Patient / Doctor Scheduler
	Create a patient class and a doctor class. 
	Setup a scheduling program
		A doctor can only handle 16 patients during an 8 hr work day.
"""

import subprocess
import datetime as dt

def cls():
    subprocess.call("cls", shell = True)

class patient:
    name = ""
    date = dt.date.today()
    