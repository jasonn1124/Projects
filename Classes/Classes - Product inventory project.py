# Classes - Product inventory project

"""
Program objectives
1) Product class with price, id, quantity
2) Inventory class to keep track of products. Function to find inventory value.
"""

# Imports
import subprocess

# Function - Clears screen
def cls():
	subprocess.call("cls", shell = True)

# Inventory class
class inventory:
	def __init__(self, branchName, productList = {}):
		self.name = branchName
		self.productList = productList

	def value(self):
		priceTally = 0
		for i in self.productList:
			priceTally += (self.productList[i].price * self.productList[i].quantity)
		print "Value of the inventory of {0} is {1} gold.".format(self.name, priceTally)
		
# Product class
class product:
	def __init__(self, productName, price, id, quantity):
		self.productName = productName
		self.price = price
		self.id = id
		self.quantity = quantity
		print "{0} added to store inventory.".format(self.productName)

	def stockCheck(self):
		if self.quantity == 0:
			print "{0} is out of stock.".format(self.productName)
		else:
			print "There are {0} of {1} in stock. Selling price is {2} gold each.".format(self.quantity, self.productName, self.price)

	def restock(self, quantitybought):
		self.quantity += quantitybought
		print "{0} (ID: {1}) resupplied by {2}. Stock is now {3}.".format(self.productName, self.id, quantitybought, self.quantity)
	
	def setPrice(self, newPrice):
		self.price = newPrice
		print "The price of {0} has been changed to {1}.".format(self.productName, self.price)

# Function - Menu - Add new product
def newProduct():
	cls()
	print "Product inventory project"
	newID = (len(singaporeStore.productList)+1)
	print "{0} items are in the product list.".format(len(singaporeStore.productList))
	print "\nMaking new entry as product ID: {0}".format(newID)
	newName = raw_input("Please enter product name: ")
	# Input check for product price
	inputLoop = True
	while inputLoop == True:
		try:
			newPrice = int(raw_input("Please enter product price: "))
		except ValueError:
			print "\nPlease enter numbers only."
		else:
			inputLoop = False
	# Input check for product quantity
	inputLoop = True
	while inputLoop == True:
		try:
			newQuantity = int(raw_input("Please enter product stock: "))
		except ValueError:
			print "\nPlease enter numbers only."
		else:
			inputLoop = False
	"""!!! Need to add product here."""
	singaporeStore.productList[newName] = product(newName, newPrice, newID, newQuantity)
	print "\nAdded {0} of {1} (ID: {2}) at {3} gold each.".format(newQuantity, newName, newID, newPrice)

# Function - Menu - List products
def showProductList():
	cls()
	print "Product inventory project\n"
	print "List of products"
	for i in singaporeStore.productList:
		print "ID {0} - {1} | {2} units selling at {3} gold each.".format(singaporeStore.productList[i].id, singaporeStore.productList[i].productName, singaporeStore.productList[i].quantity, singaporeStore.productList[i].price)
	raw_input("End of product listings")

# Initialize inventory
singaporeStore = inventory("Singapore")

# User interface
programLooping = True
while programLooping == True:
	cls()
	print "Product inventory project\n"
	print "Inventory 'Singapore' initialized."
	userInput = raw_input("ADD item | LIST items | VALUE of inventory | EXIT\n").lower()
	if userInput == "add":
		newProduct()
	elif userInput == "list":
		showProductList()
	elif userInput == "value":
		singaporeStore.value()
	elif userInput == "exit":
		programLooping = False
	else:
		print "Error."
		
	

	raw_input("End of program loop")