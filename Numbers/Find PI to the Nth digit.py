# Numbers - Find PI to the Nth Digit

# 1) Accept user_input as integer, store as variable 'digits'.
# 2) Round PI to 'digits', store as variable 'roundedPI'.
# 3) Print roundedPI.

import math
import decimal

isRunning = True

while isRunning == True:
	print "Please enter the number of digits you want for PI."
	digits = raw_input("Number of digits: ")

	if digits == "":
		print "Please enter a number!"
		raw_input()
	elif int(digits) <= 0:
		print "Please enter a positive number!"
		raw_input()
	elif int(digits) >= 12:
		print "Can only print up to 11 digits of PI."
		raw_input()
	else:
		digits = int(digits)
		roundedPI = round(math.pi, digits)
		print roundedPI
		raw_input()
		isRunning = False
