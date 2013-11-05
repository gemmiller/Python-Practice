#This script computes the total amount for an order of mousetraps
#costing 2.00 each for the first 50 and 1.50 each thereafter

numTraps = input("How many mousetraps? ")
BOX = 50
shipping = 5
numBoxes = 0
cost = 2

numBoxes = numTraps/BOX
if numTraps%BOX!=0:
	numBoxes+=1

shipping *= numBoxes
print "Shipping:",shipping
total = (numTraps*cost) + shipping
print "Total:",total
