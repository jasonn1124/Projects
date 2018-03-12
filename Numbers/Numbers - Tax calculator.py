# Numbers - Tax Calculator (WIP)


""" 
1) User inputs amount.
2) User inputs whether service charge is included. Default 10%.
3) Returns full price.
4) Optional: Splitting of bill by number of people.
5) Optional: Rounding of split bill to nearest dollar.
"""

# Imports
import subprocess

# Sets default variables
GST = 0.07
SvcCharge = 0.10

# Function - Clears screen
def cls():
	subprocess.call("cls", shell = True)
	
# Function - Converts from decimal to percentage
def convertToPercent(input):
	output = input * 100
	return output

# Function - Converts from percentage to decimal
def convertToDecimal(input):
	output = input / 100
	return output
	
# Function - Settings
def progSettings():
	global GST
	global SvcCharge	
	settingsLoop = True
	while settingsLoop == True:
		cls()
		print "Tax Calculator - Settings\n"
		print "GST - {0:.2%}\nService charge - {1:.2%}\n".format(GST,SvcCharge)
		try:
			newGST = int(raw_input("\nPlease enter a number from 1 to 100, to set the percentage of GST.\n"))
			GST = convertToDecimal(float(newGST))
			newSvcCharge = int(raw_input("\nPlease enter a number from 1 to 100, to set the percentage of service charge.\n"))
			SvcCharge = convertToDecimal(float(newSvcCharge))
		except ValueError:
			print "Please input whole numbers only!"
			raw_input()
		settingsLoop = False
	
# Loops until user goes to settings or provides a proper input.
inputLoop = True
while inputLoop == True:	
	# Information for users
	cls()
	print "Tax calculator - Main\n"
	print "GST - {0:.2%}\nService charge - {1:.2%}\n".format(GST,SvcCharge)
	print "Input the cost directly, or type 'settings' to change the percentages.\n"
	# Requests input and acts accordingly.
	userInput = raw_input(">>> ")
	if userInput == "settings":
		progSettings()
	else:
		# Makes sure input is a float, continue if so, loop if not.
		try:
			userInputFloat = float(userInput)
		except ValueError:
			print "\nPlease enter a valid number.\n"
			raw_input()
		else:
			inputLoop = False

# Input accepted, determine if split.			
inputLoop = True
while inputLoop == True:
	# Clears and displays some values.
	cls()
	print "Tax calculator - Details\n"
	print "GST - {0:.2%}\nService charge - {1:.2%}".format(GST,SvcCharge)
	print "Amount entered - {0:.2f}\n".format(userInputFloat)
	userInput = raw_input("\nIs the total cost going to be split? (Y/N) ")
	if userInput.lower() == "y":
		splitCost = True
		inputLoop = False
	elif userInput.lower() == "n":
		splitCost = False
		inputLoop = False
	else:
		print "\nPlease only enter either 'y' for YES, or 'n' for NO."
		raw_input()

# If split, requests how much to split into. Skips this part otherwise.
if splitCost == True:
	inputLoop = True
	while inputLoop == True:
		cls()
		print "Tax calculator - Details\n"
		print "GST - {0:.2%}\nService charge - {1:.2%}".format(GST,SvcCharge)
		print "Amount entered - {0:.2f}\n".format(userInputFloat)
		try:
			userInput = int(raw_input("How many parts should the final cost be split into? "))
		except ValueError:
			print "Please enter numbers only!"
			raw_input()
		else:
			splitNumber = userInput
			inputLoop = False

# Starts calculations		
cls()
print "Tax calculator - Calculations\n"
print "Original cost - ${0:.2f}".format(userInputFloat)
print "GST - {0:.2%}\nService charge - {1:.2%}\n".format(GST,SvcCharge)
print "GST costs ${0:.2f}".format(userInputFloat * GST)
print "Service charge costs ${0:.2f}".format(userInputFloat * SvcCharge)
print "Additional costs add up to a total of ${0:.2f}\n".format(userInputFloat * GST + userInputFloat * SvcCharge)
print "The total is ${0:.2f}".format(userInputFloat + userInputFloat * GST + userInputFloat * SvcCharge)

# Add-on if cost is to be split
if splitCost == True:
	print "The cost per part is ${0:.2f}".format((userInputFloat + userInputFloat * GST + userInputFloat * SvcCharge)/splitNumber)

raw_input("End of program")

