# Classic algorithms - Collatz Conjecture - 

"""
1) Accepts integer input of > 1.
2) Record number of steps needed for target to reach 1.
3) Algorithm of : If n is even, divide by 2. If n is odd, multiply by 3 and add 1.
"""

# Imports
import subprocess

# Function - Clears screen
def cls():
	subprocess.call("cls", shell = True)
	
# Program loop start
isRunning = True
while isRunning == True:
	
	# Prompts for input, checks that it is a whole number.
	inputCheckActive = True
	while inputCheckActive == True:
		cls()
		userInput = raw_input("Classic Algorithms - Collatz Conjecture\nPlease enter a number:\n")
		if userInput.isdigit() == False:
			print "\nPlease enter whole numbers only!"
			raw_input()
		elif int(userInput) == 1:
			print "\nPlease enter a number greater than 1."
			raw_input()
		else:
			targetInteger = int(userInput)
			inputCheckActive = False
	# Input is valid, commence algorithm loop
	numberOfLoops = 0
	while targetInteger != 1:
		if targetInteger % 2 == 0:
			targetInteger /= 2
		else:
			targetInteger = (targetInteger * 3) + 1
		numberOfLoops += 1
		print targetInteger
	print "\nThe algorithm has looped %i times." % (numberOfLoops)	
	print "Algorithm complete."
		
	print "\n\n\nEnd of program, looping..\n"
	raw_input()