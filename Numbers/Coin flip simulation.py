# Numbers - Coin flip simulation

"""
1) Randomize a 50/50 to simulate a coin flip.
2) Record result. Add to record of previous results.
"""

import random
import subprocess

isRunning = True
headsCounter = 0
tailsCounter = 0

def cls():
	subprocess.call('cls', shell = True)

def printOutcome(string):
	cls()
	print "The coin landed, %s was face up!\n" % (string)
	print "The coin has landed on heads %i times and on tails %i times." % (headsCounter, tailsCounter)
	raw_input("Press enter to flip another coin!")

while isRunning == True:
	cls()
	print "Press enter to flip a coin!."
	raw_input()
	
	flipOutcome = random.randint(0,1)
	if flipOutcome == 0:
		#Simulate heads.
		headsCounter += 1
		printOutcome("heads")
	elif flipOutcome == 1:
		#Simulate tails.
		tailsCounter += 1
		printOutcome("tails")
	
