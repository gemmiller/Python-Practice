# takes in a list of integers and displays a barchart of it
def display_barchart(list):
	for i in list:
		for j in range(list[i]):
			print "*", end = ""
		print ""

list = [1,2,3,4,5,6]
display_barchart(list)
