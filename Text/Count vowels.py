# Text - Count vowels

# Objectives
"""
1) Accepts strings only.
2) Tally vowels and report them.
3) Optional: Tally individual vowels.
"""

import subprocess

# Function - Clears screen.
def cls():
	subprocess.call("cls", shell = True)
	
# Function - Filters input to allow strings only.
def checkIfString(checkInput):
	if checkInput == "":
		print "No input was detected. Please type something."
		raw_input()
	elif checkInput.isdigit() == True:
		print "Please enter at least one letter."
		raw_input()
	else:
		return True
		
# Function - Counts vowels and tallies them.
def countVowels(countInput):
	# Declare dict variable to store vowel counts.
	numberOfVowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
	# Converts string to list, compares each element in list.
	countInput_List = list(countInput)
	# Iterates through each element in the list, adding to respective counts if element is a vowel.
	for i in countInput_List:
		if i == "a":
			numberOfVowels["a"] += 1
		if i == "e":
			numberOfVowels["e"] += 1
		if i == "i":
			numberOfVowels["i"] += 1
		if i == "o":
			numberOfVowels["o"] += 1
		if i == "u":
			numberOfVowels["u"] += 1
	return numberOfVowels

# Starts program loop, keeps looping, no exit.
isLooping = True
while isLooping == True:	
	cls()
	# Takes user input and saves it for processing downstream.
	targetString = raw_input("Please enter a string:\n")
	if checkIfString(targetString) == True:
		cls()
		print targetString + "\n"
		# Converts sentence to lowercase.
		targetString = targetString.lower()
		countResults = countVowels(targetString)
		totalVowels = 0
		# Collates results and prints as sentences while totalling vowels.
		for i, v in countResults.iteritems():
			totalVowels += v
			print str(v) + " of letter '" + i + "' was detected."
		print "\nA total of %i vowels were detected.\n" % (totalVowels)
	raw_input("Press enter to continue.")
