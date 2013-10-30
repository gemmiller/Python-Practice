from math import sqrt
# Takes an integer and prints of wether it is a perfect number or not
def find_perfect(perfect):
	sum = 1
	for i in range(2,int(sqrt(perfect)+1)):
		if(i%perfect==0):
			sum+= i + perfect/i
	if(sum == perfect):
		print "Perfect number"
	else:
		print "Not a perfect number"


a = input()

find_perfect(a)