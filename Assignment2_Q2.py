#Counts number of even numbers entered till user enters 'q'
def find_even_count():
	a = 'v'
	count = 0
	while(a != 'q'):
		a = raw_input()
		if(is_number(a)):
			num = int(a)
			if(num%2==0):
				count+=1
	print count, "even numbers"

#checks to see if a value is a number
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


find_even_count()
