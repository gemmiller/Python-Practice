def find_average():
	count = total = 0
	value = raw_input("Enter in a number or 'q' to quit: ")
	while value != "q":
		check = checkNumber(value)
		if check["isNumber"]:
			total += check["result"]
			count += 1
		else:
			print "Input value must be an number or 'q' to quit"
		value = raw_input("Enter in a number or 'q' to quit: ")
	if total > 0:
	return total / count


def checkNumber(value):
	try:
		x = float(value)
		return {"isNumber":True,"result":x}
	except:
		return {"isNumber":False, "result":None}
