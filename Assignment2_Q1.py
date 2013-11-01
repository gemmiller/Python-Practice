import math
# Takes an integer and prints of wether it is a perfect number or not
def find_perfect(perfect):
	sum = 1
	top = math.ceil(math.sqrt(perfect)) + 1
	for i in range(2,int(top)):
		if(perfect%i==0):
			sum+= i + perfect/i
	if(sum == perfect):
		print "Perfect number"
	else:
		print "Not a perfect number"





