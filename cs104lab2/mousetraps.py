#This script computes the total amount for an order of mousetraps
#costing 2.00 each for the first 50 and 1.50 each thereafter

num = input("How many mousetraps? ")
ans = raw_input("Are you an Iowa resident (y/n)? ")

if num <= 50:
	total = num * 2.00
else:
	first = 50*2.00
	extra = (num - 50)*1.50
	total = first + extra
print "Subtotal:", total

if ans == "y":
	total += total*.069
	print "Tax 6.9"

print "Total:", total