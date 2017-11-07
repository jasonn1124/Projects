# Numbers - Find cost of tile to cover W x H floor

"""
1) Allow user to input cost of tiles per meter^2.
2) Allow user to input width and length of floor.
3) Calculate and display area to be covered, as well as cost and 7% GST tax in Singapore.
"""

import subprocess
from decimal import *
getcontext().prec = 4

def cls():
	subprocess.call("cls", shell = True)

print "Welcome, this tool calculates the cost of tiling a rectangular room.\n"
tileCost = raw_input("Please enter the cost of tiles per square metre: ")
roomWidth = raw_input("Please enter the width of the room in metre: ")
roomLength = raw_input("Please enter the length of the room in metre: ")

roomArea = Decimal(roomWidth) * Decimal(roomLength)
roomCost = Decimal(roomArea) * Decimal(tileCost)
roomCostTaxed = Decimal(roomCost) * Decimal(1.07)

cls()
print "A room measuring %s metres by %s metres has an area of %s square metres." % (roomWidth, roomLength, roomArea)
print "At $%i per square metre, the total cost would be $%i, or $%i if including GST." % (Decimal(tileCost), roomCost, roomCostTaxed)
