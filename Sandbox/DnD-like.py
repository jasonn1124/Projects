"""
Tryin'a make something DnD-like..
"""

import subprocess
from random import randint
import msvcrt	# For "Press any key to continue.."s

def cls():
	subprocess.call('cls', shell = True)
	
def wait():
	msvcrt.getch()

class entity:
	def __init__(
					self, 
					name = "Unknown", 
					statStr = 0,
					statDex = 0,
					statCon = 0,
					statInt = 0,
					statWis = 0,
					statCha = 0,
					currentHealth = 0, 
					maxHealth = 0, 
					isAlive = True
					):
		# Initialise with name, currentHealth, maxHealth, currentMana, maxMana, isAlive
		self.name = name
		self.statStr = statStr
		self.statDex = statDex
		self.statCon = statCon
		self.statInt = statInt
		self.statWis = statWis
		self.statCha = statCha
		self.currentHealth = currentHealth
		self.maxHealth = maxHealth
		self.isAlive = isAlive
	
	def reduceHealth(self, amount):
		# Reduces hp of entity according to damage taken.
		self.currentHealth -= amount
		if self.currentHealth <= 0:
			self.currentHealth = 0
			self.isAlive = False
	
	def increaseHealth(self, amount):
		self.currentHealth += amount
		if self.currentHealth > self.maxHealth:
			self.currentHealth = self.maxHealth
				
	def showStats(self):
		print("\nName: {}\nHealth: {}/{}".format(self.name, self.currentHealth, self.maxHealth))
		
def display(title, header, content, response):
	cls()
	print(title)
	if header != "":
		print(header + "\n")
	print(content + "\n")
	print(response)
	
def checkAlive():
	if playerChar.currentHealth == 0:
		print("Oh dear, you are dead!")
		isRunning = False
		return False
	elif enemyChar.currentHealth == 0:
		print("You won!")
		isRunning = False
		return False

def newChar():
	# 6 ability scores, 4d6 rolls for each, removing the lowest score and summing the rest.
	counter_statRolls = 6
	statRolls = []
	while counter_statRolls != 0:
		diceRoll4d6 = []
		summedRoll = 0
		counter_4d6 = 4
		while counter_4d6 != 0:
			diceRoll4d6.append(randint(1,6))
			counter_4d6 -= 1
		diceRoll4d6 = sorted(diceRoll4d6)
		diceRoll4d6.pop(0)
		for i in range(0, len(diceRoll4d6)):
			summedRoll += diceRoll4d6[i]
		statRolls.append(summedRoll)
		counter_statRolls -= 1	

	# Prompts user to assign stat rolls to whichever stat they want.
	statNames = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
	userChoice = []
	counter_statInput = 0
	while counter_statInput != 6:
		cls()
		print(
			"Assign scores\n\nSelecting for {0}.\nPlease select which score should be assigned to {0}.".format(statNames[counter_statInput])
			)
		print("List of scores remaining: {}".format(statRolls))
		try:
			userInput = int(input(">> "))
		except ValueError:
			print("Please enter integers only!")
			wait()
		else:
			try:
				statRolls.remove(userInput)
			except ValueError:
				print("There is no such value in the list of scores. Please pick a valid score.")
				wait()
			else:
				userChoice.append(userInput)
				counter_statInput += 1
	print(userChoice)
			# !!! Search statRolls for userInput, if present, remove from list and assign, then loop. Else, flag error and loop without assigning.
# App start
playerChar = entity("Hiro", 0, 0, 0, 0, 0, 0, 100, 100, True)
enemyChar = entity("Rat", 0, 0, 0, 0, 0, 0, 10, 10, True)
newChar()
wait()
isRunning = True
while isRunning == True:
	display()
	if checkAlive() == False:
		print("\n End")
		isRunning = False
	else:
		print("\nBattle!")
		inputLoop = True
	while inputLoop == True:
		try:
			userInput = (input("\n(A)ttack | (D)odge | (E)xit\n")).lower()
		except ValueError:
			print("Command not recognized, please enter appropriate command.")
		else:
			if userInput == "a":
				damage = randint(1,10)
				enemyChar.reduceHealth(damage)
				print("\nYou hit {} for {} damage.".format(enemyChar.name, damage))
				damage = randint(1,10)
				playerChar.reduceHealth(damage)
				input ("You were hit for {} damage.".format(damage))
				inputLoop = False
			elif userInput == "d":
				print("Dodge attempted")
				inputLoop = False
			elif userInput == "e":
				print("Exiting...")
				inputLoop = False
				isRunning = False
				
	

	
wait()
		