#Counts number of even numbers entered till user enters 'q'
def find_even_count():
	a = 'v'
	count = 0
	while(a != 'q'):
		a = raw_input()
		num = int(a)
		if(num%2==0):
			count+=1
	print count, "even numbers"
