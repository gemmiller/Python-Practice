from math import ceil , sqrt
import factors
# Takes an integer and prints of wether it is a perfect number or not
def find_perfect(perfect):
	sum = 1
	top =ceil(sqrt(perfect)) + 1
	for i in range(2,int(top)):
		if(perfect%i==0):
			sum+= i + perfect/i
	if(sum == perfect):
		print "Perfect number"
	else:
		print "Not a perfect number"



def find_perfectFast(perfect):
	factors = factors.findPrimeFactors(perfect)
	if(sum(factors)+1==perfect):
		print "Perfect number"
	else:
		print "Not a perfect number"




